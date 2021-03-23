import i2c_LCD_driver
from time import *

mylcd = i2c_LCD_driver.lcd()

mylcd.lcd_display_string("Hello World!", 1)