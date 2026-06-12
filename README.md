Installation


1. Update Termux

pkg update -y && pkg upgrade -y


2. Install Requirements

pkg install git python -y


3. Allow Storage Access

termux-setup-storage

Press Allow when Android asks for permission.


4. Clone Repository

git clone https://github.com/pars1500/cfscanner.git

cd cfscanner


5. Run Installer

bash install.sh


6. Start Application

python app.py
