# RaspiPhono
## Mini gramophone with raspberry pi zero


[Instructable](https://www.instructables.com/id/RaspiPhono)

---

### Dependencies

`pip3 install pygame`

---

### Setup

* Config I2S

`curl -sS https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/i2samp.sh | bash`

<em>[more info](https://learn.adafruit.com/adafruit-max9857-i2s-class-d-mono-amp/raspberry-pi-usage)</em>

* Setup powerup and powerdown button, pin 3(SCL)

Add in the file `/boot/config.txt`: `dtoverlay=gpio-shutdown`

<em>[more info](https://www.stderr.nl/Blog/Hardware/RaspberryPi/PowerButton.html)</em>

*  Config startup script

Copy ``raspiphonoinit.sh`` to init directory

`$ sudo cp raspiphonoinit.sh /etc/init.d`

`$ sudo update-rc.d raspiphonoinit defaults`