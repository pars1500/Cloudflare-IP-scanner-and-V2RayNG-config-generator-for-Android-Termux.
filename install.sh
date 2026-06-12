#!/data/data/com.termux/files/usr/bin/bash

clear

echo "========================================"
echo "         CFScanner Installer"
echo "========================================"
echo ""

pkg update -y

pkg install python -y

termux-setup-storage

chmod +x *.py

echo ""
echo "========================================"
echo " Installation Completed Successfully"
echo "========================================"
echo ""
echo "Run the application with:"
echo ""
echo "python app.py"
echo ""
