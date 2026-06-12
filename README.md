CFScanner

Cloudflare IP Scanner & V2RayNG Config Generator for Android Termux

Features

- Download official Cloudflare IPv4 ranges
- Generate random Cloudflare IPs
- Multi-threaded scanning
- Save Top 50 fastest endpoints
- Generate V2RayNG configs automatically
- Interactive menu
- Android Termux compatible

---

Installation

pkg update -y
pkg install git python -y

git clone https://github.com/pars1500/cfscanner.git

cd cfscanner

bash install.sh

---

Run Application

python app.py

---

Output Files

Scanner Results:

/sdcard/Download/good_cf.txt

Generated Configs:

/sdcard/Download/generated_configs.txt

---

Menu

1. Scan Cloudflare IPs
2. Generate V2RayNG Configs
3. Show Output Files
4. Show Project Files
5. About
0. Exit

---

Persian Documentation

See:

README_FA.md

---

License

MIT License

---

Author

pars1500
