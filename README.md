# Cloudflare Scanner for Termux

Cloudflare IP scanner, latency analyzer, and V2RayNG config generator for Android Termux.

## Features

- Discover active Cloudflare IPs
- Test common Cloudflare ports
- Filter IPs by ping range
- Save good IPs to TXT file
- Export results to Android Downloads folder
- Generate new V2RayNG configs from a base config
- Optimized for Termux

## Target Ping Range

```text
100ms - 300ms


Tested Ports
Plain text
443
2053
2083
2087
2096
8443
Output Files
Plain text
good_cf.txt
generated_configs.txt
Project Goals
Find active Cloudflare IPs with good latency.
Save discovered IPs into a text file on mobile storage.
Generate new V2RayNG configs using discovered IPs and ports.
Requirements
Android
Termux
Python 3
Usage
Bash
python main.py
License
MIT License
