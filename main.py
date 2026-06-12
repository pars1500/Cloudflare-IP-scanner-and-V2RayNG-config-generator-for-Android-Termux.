from concurrent.futures import ThreadPoolExecutor, as_completed

from cloudflare_ranges import get_cloudflare_ipv4_ranges
from ip_generator import generate_random_ips
from scanner import test_ip


GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"


MIN_LATENCY = 100
MAX_LATENCY = 300

COUNT_PER_RANGE = 334
MAX_WORKERS = 200
TOP_RESULTS = 50

OUTPUT_FILE = "/sdcard/Download/good_cf.txt"


def save_results(results):
    with open(OUTPUT_FILE, "w") as file:
        for item in results:
            line = f"{item['ip']}:{item['port']} ping={item['latency']}ms"
            file.write(line + "\n")

    print(f"\n{GREEN}Results saved:{RESET} {OUTPUT_FILE}")


def main():

    print(f"{CYAN}{'=' * 60}{RESET}")
    print(f"{BOLD}{GREEN}CFScanner v1.2{RESET}")
    print(f"{CYAN}{'=' * 60}{RESET}")

    print("Loading Cloudflare ranges...")

    ranges = get_cloudflare_ipv4_ranges()

    if not ranges:
        print(f"{RED}No Cloudflare ranges found.{RESET}")
        return

    ips = generate_random_ips(
        ranges,
        count_per_range=COUNT_PER_RANGE
    )

    print(f"Target scan size: {len(ips)} IPs")
    print(f"Best results to save: {TOP_RESULTS}")
    print()

    good_results = []

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:

        tasks = [
            executor.submit(test_ip, ip)
            for ip in ips
        ]

        total = len(tasks)
        completed = 0

        for task in as_completed(tasks):

            completed += 1

            percent = int(
                (completed / total) * 100
            )

            results = task.result()

            for item in results:

                latency = item["latency"]

                if MIN_LATENCY <= latency <= MAX_LATENCY:
                    good_results.append(item)

            best_ping = "-"

            if good_results:
                best_ping = min(
                    x["latency"]
                    for x in good_results
                )

            print(
                f"\r{GREEN}{percent:3d}%{RESET} | "
                f"Scanned:{completed}/{total} | "
                f"Good:{len(good_results)} | "
                f"Best:{best_ping}ms",
                end=""
            )

    print("\n")

    total_good = len(good_results)

    good_results.sort(
        key=lambda x: x["latency"]
    )

    good_results = good_results[:TOP_RESULTS]

    print(f"{CYAN}{'=' * 60}{RESET}")
    print(f"{GREEN}SCAN COMPLETED{RESET}")
    print(f"{CYAN}{'=' * 60}{RESET}")

    print(f"Total scanned : {total}")
    print(f"Good found    : {total_good}")
    print(f"Saved top     : {len(good_results)}")

    if good_results:

        best = good_results[0]

        print(
            f"Best ping     : "
            f"{best['latency']} ms"
        )

        print(
            f"Best endpoint : "
            f"{best['ip']}:{best['port']}"
        )

        save_results(good_results)

    else:
        print(f"{RED}No good IP found.{RESET}")

    print(f"{CYAN}{'=' * 60}{RESET}")


if __name__ == "__main__":
    main()
