from concurrent.futures import ThreadPoolExecutor, as_completed

from cloudflare_ranges import get_cloudflare_ipv4_ranges
from ip_generator import generate_random_ips
from scanner import test_ip


MIN_LATENCY = 100
MAX_LATENCY = 300

COUNT_PER_RANGE = 50
MAX_WORKERS = 50

OUTPUT_FILE = "/sdcard/Download/good_cf.txt"


def save_results(results):
    with open(OUTPUT_FILE, "w") as file:
        for item in results:
            line = f"{item['ip']}:{item['port']} ping={item['latency']}ms"
            file.write(line + "\n")

    print(f"\nSaved results to {OUTPUT_FILE}")


def main():

    print("=" * 50)
    print("Cloudflare Scanner for Termux")
    print("=" * 50)

    print("Fetching Cloudflare IP ranges...")

    ranges = get_cloudflare_ipv4_ranges()

    if not ranges:
        print("No Cloudflare ranges found.")
        return

    print(f"Found {len(ranges)} Cloudflare ranges.")

    print("Generating random IPs...")

    ips = generate_random_ips(
        ranges,
        count_per_range=COUNT_PER_RANGE
    )

    print(f"Generated {len(ips)} IPs.")

    print("Scanning started...\n")

    good_results = []

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:

        tasks = [
            executor.submit(test_ip, ip)
            for ip in ips
        ]

        for task in as_completed(tasks):

            results = task.result()

            for item in results:

                latency = item["latency"]

                if MIN_LATENCY <= latency <= MAX_LATENCY:

                    good_results.append(item)

                    print(
                        f"[GOOD] "
                        f"{item['ip']}:{item['port']} "
                        f"ping={latency}ms"
                    )

    good_results.sort(
        key=lambda x: x["latency"]
    )

    if good_results:

        save_results(good_results)

        print(
            f"\nTotal good results: "
            f"{len(good_results)}"
        )

    else:
        print("No good IP found.")


if __name__ == "__main__":
    main()
