from config_generator import read_good_ips, generate_v2ray_configs, save_configs

base_config = input("Paste your V2RayNG config: ")

ips = read_good_ips()
configs = generate_v2ray_configs(base_config, ips, limit=20)

save_configs(configs)

print("Generated configs:")
for config in configs:
    print(config)
