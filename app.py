import os
from main import main as run_scanner
from generate import main as run_generator


def clear_screen():
    os.system("clear")


def show_banner():
    print("=" * 50)
    print("CFScanner for Termux")
    print("Cloudflare IP Scanner & V2RayNG Generator")
    print("=" * 50)


def show_menu():
    print()
    print("[1] Scan Cloudflare IPs")
    print("[2] Generate V2RayNG Configs")
    print("[3] Open Output Folder")
    print("[4] Show Files")
    print("[0] Exit")
    print()


def open_output_folder():
    print("Output files:")
    print("/sdcard/Download/good_cf.txt")
    print("/sdcard/Download/generated_configs.txt")


def show_files():
    os.system("ls -lh")
    print()
    os.system("ls -lh /sdcard/Download/good_cf.txt 2>/dev/null")
    os.system("ls -lh /sdcard/Download/generated_configs.txt 2>/dev/null")


def main():
    while True:
        clear_screen()
        show_banner()
        show_menu()

        choice = input("Select an option: ").strip()

        if choice == "1":
            clear_screen()
            run_scanner()
            input("\nPress Enter to return to menu...")

        elif choice == "2":
            clear_screen()
            run_generator()
            input("\nPress Enter to return to menu...")

        elif choice == "3":
            clear_screen()
            open_output_folder()
            input("\nPress Enter to return to menu...")

        elif choice == "4":
            clear_screen()
            show_files()
            input("\nPress Enter to return to menu...")

        elif choice == "0":
            print("Goodbye.")
            break

        else:
            print("Invalid option.")
            input("\nPress Enter to return to menu...")


if __name__ == "__main__":
    main()
