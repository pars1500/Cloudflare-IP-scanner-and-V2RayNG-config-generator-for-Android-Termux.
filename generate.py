from config_generator import read_good_ips, generate_v2ray_configs, save_configs


def main():
    print("=" * 50)
    print("V2RayNG Config Generator")
    print("=" * 50)

    base_config = input("Paste your V2RayNG config: ")

    count = input("How many configs do you want? default=20: ").strip()

    if count == "":
        count = 20
    else:
        count = int(count)

    ips = read_good_ips("/sdcard/Download/good_cf.txt")

    configs = generate_v2ray_configs(
        base_config,
        ips,
        limit=count
    )

    save_configs(
        configs,
        "/sdcard/Download/generated_configs.txt"
    )

    print("\n")
    print("=" * 50)
    print("COPY FROM HERE")
    print("=" * 50)
    print()

    for config in configs:
        print(config)

    print()
    print("=" * 50)
    print(f"TOTAL CONFIGS: {len(configs)}")
    print("=" * 50)

    print("\nSaved to:")
    print("/sdcard/Download/generated_configs.txt")


if __name__ == "__main__":
    main()
