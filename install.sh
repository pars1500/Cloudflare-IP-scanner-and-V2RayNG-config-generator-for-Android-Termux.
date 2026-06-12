#!/bin/bash

pkg update -y
pkg install python git -y
termux-setup-storage

echo "Installation completed."
echo "Run scanner with:"
echo "python main.py"
echo ""
echo "Generate configs with:"
echo "python generate.py"
