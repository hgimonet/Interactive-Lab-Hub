import time
import board
import busio

import adafruit_mpr121

from LCD_driver import i2c_LCD_driver as LDC

lcd = LDC.lcd()

i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

BOWL_ID = 5
BUTTON_ID = 6

lick_count = 0
while True:
    if mpr121[BUTTON_ID].value:
        lick_count = 0
    if mpr121[BOWL_ID].value:
        lick_count +=1
    lcd.lcd_write('Lick Count: %4d'%(lick_count))
    time.sleep(1)