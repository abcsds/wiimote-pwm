#!/bin/bash
echo "Installing..."
sudo apt-get update
sudo apt-get install --no-install-recommends bluetooth
sudo apt-get install python-cwiid
git clone https://github.com/sarfata/pi-blaster.git
cd pi-blaster
sudo apt-get install autoconf
./autogen.sh
./configure
make
sudo make install
ln -sfv pi-blaster /usr/bin/pi-blaster
cd ..
python wiimote-pwm.py
echo "Installation ready"
