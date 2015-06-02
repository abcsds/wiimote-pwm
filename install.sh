#!/bin/bash
echo "Installing..."
sudo apt-get update
sudo apt-get install -y --no-install-recommends bluetooth
sudo apt-get install -y python-cwiid
git clone https://github.com/sarfata/pi-blaster.git
cd pi-blaster
sudo apt-get install autoconf
./autogen.sh
./configure
make
sudo make install
ln -sfv pi-blaster /usr/bin/pi-blaster
cd ..
echo "Installation ready"
echo "Run python wiimote-pwm.py"
