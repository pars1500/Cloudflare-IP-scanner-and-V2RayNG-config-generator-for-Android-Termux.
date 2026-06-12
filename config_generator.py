from urllib.parse import urlparse, urlunparse


def read_good_ips(file_path="/sdcard/Download/good_cf.txt"):
    results = []

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            ip_port = line.split()[0]
            ping_text = line.split("ping=")[1].replace("ms", "")

            ip, port = ip_port.split(":")
            ping = int(ping_text)

            results.append({
                "ip": ip,
                "port": port,
                "ping": ping
            })

    results.sort(key=lambda x: x["ping"])
    return results


def generate_v2ray_configs(base_config, ip_list, limit=20):
    configs = []

    parsed = urlparse(base_config)
    username = parsed.username

    for index, item in enumerate(ip_list[:limit], start=1):
        new_netloc = f"{username}@{item['ip']}:{item['port']}"

        new_config = urlunparse((
            parsed.scheme,
            new_netloc,
            parsed.path,
            parsed.params,
            parsed.query,
            f"FAST-{index}-{item['ip']}-{item['port']}-{item['ping']}ms"
        ))

        configs.append(new_config)

    return configs


def save_configs(configs, output_file="/sdcard/Download/generated_configs.txt"):
    with open(output_file, "w") as file:
        for config in configs:
            file.write(config + "\n")

    print(f"Saved configs to {output_file}")
