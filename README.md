# PWM with wiimote
This script generates 3 PWM on pins 23, 24, and 25 of raspberry GPIO, coming from the values of x, y and z accelerometers from a wiimote.

## Requirements
### Hardware
 - Raspberry
 - bluetooth dongle
 - wiimote

### Software
This code uses linux bluetooth module and [pi-blaster](https://github.com/sarfata/pi-blaster), they should be installed as specified here before running the program. The [installation script](#installation-script) runs these installations for you.

## Manual Installation

### Install bluetooth
`sudo apt-get install --no-install-recommends bluetooth`

If it's working `sudo service bluetooth status` should return `bluetooth is running`.

### Install python-cwiid
`sudo apt-get install python-cwiid`

### Install pi-blaster
```shell
git clone https://github.com/sarfata/pi-blaster.git
cd pi-blaster
sudo apt-get install autoconf
./autogen.sh
./configure
make
sudo make install
ln -sfv pi-blaster /usr/bin/pi-blaster
```
Then run in a separate console pi-blaster `pi-blaster`

### Run the program

`python wiimote-pwm.py`

## Installation script
So... this is mostly just shell, so I made a script. Run:
```shell
chmod +x install.sh
./install.sh
```

## LICENCE

This code is licensed under GPLv3.
