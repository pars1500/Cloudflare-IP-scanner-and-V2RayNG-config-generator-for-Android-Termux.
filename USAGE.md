Usage Guide

Install

pkg update -y
pkg install python git -y

git clone https://github.com/pars1500/Cloudflare-IP-scanner-and-V2RayNG-config-generator-for-Android-Termux..git

cd Cloudflare-IP-scanner-and-V2RayNG-config-generator-for-Android-Termux.

bash install.sh

Scan Cloudflare IPs

python main.py

Output:

/sdcard/Download/good_cf.txt

Generate V2RayNG Configs

python generate.py

Output:

/ sdcard/Download/generated_configs.txt
