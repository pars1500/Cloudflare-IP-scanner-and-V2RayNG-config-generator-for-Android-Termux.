import os
import time

from main import main as run_scanner
from generate import main as run_generator


GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"


def clear_screen():
    os.system("clear")


def pause():
    input(f"\n{YELLOW}Press Enter to return to menu...{RESET}")


def banner():
    print(f"{CYAN}{'=' * 56}{RESET}")
    print(f"{BOLD}{GREEN}                 CFSCANNER v1.1{RESET}")
    print(f"{CYAN}      Cloudflare Scanner for Android Termux{RESET}")
    print(f"{CYAN}     IP Scanner + V2RayNG Config Generator{RESET}")
    print(f"{CYAN}{'=' * 56}{RESET}")


def menu():
    print()
    print(f"{GREEN}[1]{RESET} Scan Cloudflare IPs")
    print(f"{GREEN}[2]{RESET} Generate V2RayNG Configs")
    print(f"{GREEN}[3]{RESET} Show Output Files")
    print(f"{GREEN}[4]{RESET} Show Project Files")
    print(f"{GREEN}[5]{RESET} About")
    print(f"{RED}[0]{RESET} Exit")
    print()


def show_output_files():
    print(f"{BOLD}Output Files:{RESET}\n")

    files = [
        "/sdcard/Download/good_cf.txt",
        "/sdcard/Download/generated_configs.txt",
    ]

    for file_path in files:
        if os.path.exists(file_path):
            size = os.path.getsize(file_path)
            print(f"{GREEN}[OK]{RESET} {file_path}  ({size} bytes)")
        else:
            print(f"{RED}[NOT FOUND]{RESET} {file_path}")


def show_project_files():
    print(f"{BOLD}Project Files:{RESET}\n")
    os.system("ls -lh")


def about():
    print(f"{BOLD}CFScanner v1.1{RESET}\n")
    print("A Termux-friendly Cloudflare IP scanner and V2RayNG config generator.")
    print()
    print("Features:")
    print("- Fetch official Cloudflare IPv4 ranges")
    print("- Generate random Cloudflare IPs")
    print("- Scan common Cloudflare ports")
    print("- Filter IPs by latency")
    print("- Save good results to Android Downloads")
    print("- Generate fast V2RayNG configs from the best IPs")
    print()
    print("GitHub:")
    print("https://github.com/pars1500/cfscanner")


def main():
    while True:
        clear_screen()
        banner()
        menu()

        choice = input(f"{BOLD}Select an option: {RESET}").strip()

        if choice == "1":
            clear_screen()
            banner()
            print(f"\n{YELLOW}Starting Cloudflare scan...{RESET}\n")
            time.sleep(1)
            run_scanner()
            pause()

        elif choice == "2":
            clear_screen()
            banner()
            print(f"\n{YELLOW}Starting V2RayNG config generator...{RESET}\n")
            time.sleep(1)
            run_generator()
            pause()

        elif choice == "3":
            clear_screen()
            banner()
            show_output_files()
            pause()

        elif choice == "4":
            clear_screen()
            banner()
            show_project_files()
            pause()

        elif choice == "5":
            clear_screen()
            banner()
            about()
            pause()

        elif choice == "0":
            clear_screen()
            print(f"{GREEN}Goodbye!{RESET}")
            break

        else:
            print(f"{RED}Invalid option. Please try again.{RESET}")
            time.sleep(1)


if __name__ == "__main__":
    main()
