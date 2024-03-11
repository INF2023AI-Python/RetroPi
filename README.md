# RetroPi
---

Documentation:

Installation of Debian Linux
Username retropie
Pasword raspberry

Installation of the Github Repo for the Matrix

curl https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/main/rgb-matrix.sh >rgb-matrix.sh
sudo bash rgb-matrix.sh


to run the examples you have to run the file with the parameters --led-rows=32 --led-cols=32

Problems with Matrix -> Read Doc:
https://github.com/hzeller/rpi-rgb-led-matrix?tab=readme-ov-file#if-you-have-an-adafruit-hat-or-bonnet

tried to install the rpi-fb-matrix lib to see the Screen of the Raspi on the Matrix
https://github.com/adafruit/rpi-fb-matrix
followed the tutorial on the Github Repo -> make -> ERROR with the bcm module

Bachelor thesis I found online (did a very similar project to the one we do):
https://www.christianbaun.de/Abschlussarbeiten/Dimitri_Gubermann_Bachelorarbeit_2017.pdf (S.43-45)


Debugging:

1. https://learn.adafruit.com/raspberry-pi-led-matrix-display/software
	this article describes the installation process diffrently to the thesis mentioned above
2. https://github.com/hzeller/rpi-rgb-led-matrix/blob/master/lib/Makefile
	adjustment to the CMake file -> regular to adafruit-hat and some more


Installed Kernel Headers:
sudo apt-get install raspberrypi-kernel-headers

test display worked -> screen doesnt show up -> Debug_dump file

-> Bullseye on Raspi:
installed only rpi-fb-matrix

worked out of the box

installed newest version of python
https://aruljohn.com/blog/python-raspberrypi/

took ages (2h)

installed newest version of pygame on this python env
python -m pip install requests

now works

