CFScanner - راهنمای فارسی

معرفی

CFScanner یک ابزار مخصوص ترموکس اندروید است که:

- آی‌پی‌های Cloudflare را اسکن می‌کند
- بهترین آی‌پی‌ها را بر اساس پینگ انتخاب می‌کند
- فایل خروجی ایجاد می‌کند
- کانفیگ‌های جدید V2RayNG تولید می‌کند

---

پیش نیازها

- گوشی اندروید
- برنامه Termux
- اینترنت فعال

---

نصب

دستورات زیر را اجرا کنید:

pkg update -y

pkg install git python -y

git clone https://github.com/pars1500/cfscanner.git

cd cfscanner

bash install.sh

---

اجرای برنامه

python app.py

---

اسکن آی‌پی‌های Cloudflare

در منو گزینه زیر را انتخاب کنید:

1

سپس حجم اسکن را انتخاب کنید:

1 = 1000 IP
2 = 5000 IP
3 = 10000 IP

پس از پایان اسکن بهترین نتایج در فایل زیر ذخیره می‌شوند:

/sdcard/Download/good_cf.txt

---

ساخت کانفیگ V2RayNG

در منوی اصلی گزینه زیر را انتخاب کنید:

2

سپس:

1. کانفیگ VLESS خود را وارد کنید.
2. تعداد کانفیگ خروجی را مشخص کنید.

فایل خروجی در مسیر زیر ذخیره می‌شود:

/sdcard/Download/generated_configs.txt

---

محل ذخیره فایل‌ها

نتایج اسکن:

/sdcard/Download/good_cf.txt

کانفیگ‌های تولید شده:

/sdcard/Download/generated_configs.txt

---

بروزرسانی پروژه

برای دریافت آخرین نسخه:

cd ~/cfscanner

git pull

---

رفع مشکلات رایج

اگر دسترسی حافظه صادر نشده باشد:

termux-setup-storage

اگر برنامه اجرا نشد:

pkg update

pkg upgrade

---

توسعه دهنده

pars1500

CFScanner v1.3
