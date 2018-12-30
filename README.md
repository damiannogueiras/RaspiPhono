# RaspiPhono
## Mini gramophone with raspberry pi zero


[Instructable](https://www.instructables.com/id/RaspiPhono)

---

### Dependencies

Install [pygame](https://www.pygame.org/)

`$ pip3 install pygame`


---

### Setup

* Config I2S <em>[(more info)](https://learn.adafruit.com/adafruit-max9857-i2s-class-d-mono-amp/raspberry-pi-usage)</em>

`$curl -sS https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/i2samp.sh | bash`



* Setup powerup and powerdown button, pin 3(SCL) <em>[(more info)](https://www.stderr.nl/Blog/Hardware/RaspberryPi/PowerButton.html)</em>

Add in the file `/boot/config.txt`: `dtoverlay=gpio-shutdown`


*  If you want start the script in the init

Copy `raspiphonoinit` to init directory

`$ sudo cp RaspiPhono/raspiphonoinit /etc/init.d`

Add execute permission

`$ sudo chmod 755 /etc/init.d/raspiphonoinit`

`$ sudo update-rc.d raspiphonoinit defaults`

---

### Clone and run

Clone the code

`$ git clone https://github.com/damiannogueiras/RaspiPhono.git`

And run

`$ cd RaspiPhono`

`$ python3 gramophono.py`