import ipaddress
import random


def generate_random_ips(cidr_ranges, count_per_range=100):
    ips = []

    for cidr in cidr_ranges:
        network = ipaddress.ip_network(cidr, strict=False)

        total_ips = network.num_addresses

        for _ in range(count_per_range):
            random_index = random.randint(1, total_ips - 2)
            ip = str(network[random_index])
            ips.append(ip)

    return ips

