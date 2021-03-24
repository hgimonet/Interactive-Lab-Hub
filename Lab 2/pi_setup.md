# Pi Cheat Sheet

## Connecting to the Pi

Pi Login: `ssh pi@192.168.1.77`

Pw Hint: constant

## Git Commands

To update labs: 
```
git pull upstream Spring2021
```

## Raspberry Pi Commands

to restart/shutdown:
```
sudo shutdown [-r or -h] now 
```

### [GPIO Usage](https://www.raspberrypi.org/documentation/usage/gpio/)

<img src="https://www.raspberrypi.org/documentation/usage/gpio/images/GPIO-Pinout-Diagram-2.png" width="400">

Any of the GPIO pins can be designated (in software) as an input or output pin and used for a wide range of purposes.

<img src="https://www.raspberrypi.org/documentation/usage/gpio/images/GPIO.png" width="400">

### [STEMMA QT](https://learn.adafruit.com/introducing-adafruit-stemma-qt/technical-specs)

For the STEMMA QT cables, we follow the Qwiic convention:
- Black for GND 
- Red for V+ 
- Blue for SDA
- Yellow for SCL

