# import what is needed for the shutdown button
import digitalio
import board
import time # import time functions
import os #imports OS library for Shutdown control

stopButton = digitalio.DigitalInOut(board.D23) # defines the button as an object and chooses GPIO 26

while True: #infinite loop
     if stopButton.is_pressed: #Check to see if button is pressed
        time.sleep(1) # wait for the hold time we want.
        if stopButton.is_pressed: #check if the user let go of the button
            os.system("shutdown now -h") #shut down the Pi -h is or -r will reset
    time.sleep(1) # wait to loop again so we don’t use the processor too much.