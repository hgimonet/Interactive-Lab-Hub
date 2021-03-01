import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789


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

first_line = "A: start/stop,"
second_line = "B: lap, A+B: reset"

timer_secs = 0
timer_on = False
lap = ""


while True:

    date_now = time.strftime("%m/%d/%Y")
    time_now = time.strftime("%H:%M:%S")
    timer_now = time.strftime("%H:%M:%S",time.gmtime(timer_secs))

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    if buttonB.value and not buttonA.value:  # just button A pressed
        timer_on = not timer_on
    if buttonA.value and not buttonB.value:  # just button B pressed
        lap = timer_now  # save the current timer time
    if not buttonA.value and not buttonB.value:  # both pressed
        timer_secs = 0  # reset timer
        lap = ""  # reset lap

    if timer_on:
        timer_secs += 1

    # Write  lines of text.

    y = top

    lines = [first_line, second_line]

    for text in lines:
        x = int(width / 2 - font.getsize(text)[0] / 2)
        draw.text((x, y), text, font=font, fill="#FFFFFF")
        y += font.getsize(text)[1]

    # x = int(width/2-font.getsize(date_now)[0]/2)
    # draw.text((x, y), date_now, font=font, fill="#FFFFFF")
    # y += font.getsize(date_now)[1]

    x = int(width/2-font.getsize(time_now)[0]/2)
    draw.text((x, y), time_now, font=font, fill="#FFFFFF")
    y += font.getsize(time_now)[1]

    x = int(width/2-font.getsize(timer_now)[0]/2)
    draw.text((x, y), timer_now, font=font, fill="#FFFF00")
    y += font.getsize(timer_now)[1]

    x = int(width / 2 - font.getsize(lap)[0] / 2)
    draw.text((x, y), lap, font=font, fill="#FFFFFF")

    # Display image.
    disp.image(image, rotation)
    time.sleep(1)