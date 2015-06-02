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
while :
do
    read -p "Do you whish to run on boot?" yn
        case $yn in
            [Yy]* ) echo 'bash ~/wiimote-pwm/onBoot.sh' >> ~/.bashrc;echo "done!"; break;;
            [Nn]* ) break;;
            * ) echo "Please answer yes or no.";;
        esac
done
echo "Startin pi-blaster"
sudo pi-blaster
echo "Installation ready"
echo "Run python wiimote-pwm.py"
