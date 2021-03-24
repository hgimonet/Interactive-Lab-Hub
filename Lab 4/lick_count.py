import time
import board
import busio

import adafruit_mpr121

from LCD_driver import i2c_LCD_driver as LDC

lcd = LDC.lcd()

i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

lick_count = 0
while True:
