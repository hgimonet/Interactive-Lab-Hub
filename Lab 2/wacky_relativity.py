import time, datetime
import subprocess
from PIL import Image, ImageDraw, ImageFont
# for screen display
import digitalio
import board
import adafruit_rgb_display.st7789 as st7789
# for accelerometer
import busio
import adafruit_mpu6050
# for calculating velocity
import numpy as np
from math import sqrt

# Configuration for gyrometer
i2c = busio.I2C(board.SCL, board.SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)
# reset mpu
# mpu.reset()

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)


# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# get buttons
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

bg_color = 'black'

# initialize old acceleration
accel_old = np.zeros(3)
vel = np.zeros(3)

# set the refresh time
dt = 0.0001

# initilize offsets
accel_offsets = [ 0.82114222, -0.13894366,  7.9939099 ]
gyro_offsets = [-2.36665191, -0.4468687,  -0.18727176]

mpu.reset()
mpu.sleep = False
mpu.cycle = True

relative_time = 0
relative_on = False
start_time = datetime.datetime.now()

def relativity(dt,v,c=2.99792458e3):
    return dt / sqrt(1-v**2/c**2)

while True:

    if buttonB.value and not buttonA.value:  # just button A pressed
        relative_time = 0
        start_time = datetime.datetime.now()
    # if buttonA.value and not buttonB.value:  # just button B pressed
    # if not buttonA.value and not buttonB.value:  # both pressed

    accel = np.array(mpu.acceleration) #- accel_offsets
    gyro = np.array(mpu.gyro) #- gyro_offsets

    # calculate velocity assuming accel gives displacement
    # vel = (accel_old - accel)/(dt)
    vel += accel*dt
    speed = np.linalg.norm(vel)

    date_now = time.strftime("%m/%d/%Y")
    time_now = time.strftime("%H:%M:%S")
    time_relative = (start_time + datetime.timedelta(seconds = dt)).strftime("%H:%M:%S")

    acceleration = "a: X:%.2f, Y: %.2f, Z: %.2f m/s^2"%(tuple(accel))
    velocity = "v: X:%.2f, Y: %.2f, Z: %.2f m/s" %(tuple(vel))
    gyro = "Gyro X:%.2f, Y: %.2f, Z: %.2f degrees/s"%(tuple(gyro))
    speed_print = "Speed: %.2f m/s"%(speed)
    # temp = "Temperature: %.2f C"%mpu.temperature

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # Write  lines of text.
    lines = [acceleration, velocity, speed_print, time_now, time_relative]
    y = top
    for text in lines:
        x = int(width / 2 - font.getsize(text)[0] / 2)
        draw.text((x, y), text, font=font, fill="#FFFFFF")
        y += font.getsize(text)[1]

    # Display image.
    disp.image(image, rotation)
    time.sleep(dt)
    relative_time += relativity(dt,speed)
    accel_old = accel