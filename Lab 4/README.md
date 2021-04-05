# Ph-UI!!!

For lab this week, we focus on the prototyping the physical look and feel of the device. _Make sure you read all the instructions and understand the whole of the laboratory activity before starting!_



## Prep

1. Pull the new Github Repo.
2. Readings: 

* [What do prototypes prototype?](https://www.semanticscholar.org/paper/What-do-Prototypes-Prototype-Houde-Hill/30bc6125fab9d9b2d5854223aeea7900a218f149)

* [Paper prototyping](https://www.uxpin.com/studio/blog/paper-prototyping-the-practical-beginners-guide/) is used by UX designers to quickly develop interface ideas and run them by people before any programming occurs. 

* [Cardboard prototypes](https://www.youtube.com/watch?v=k_9Q-KDSb9o) help interactive product designers to work through additional issues, like how big something should be, how it could be carried, where it would sit. 

* [Tips to Cut, Fold, Mold and Papier-Mache Cardboard](https://makezine.com/2016/04/21/working-with-cardboard-tips-cut-fold-mold-papier-mache/) from Make Magazine.

* [Surprisingly complicated forms](https://www.pinterest.com/pin/50032245843343100/) can be built with paper, cardstock or cardboard.  The most advanced and challenging prototypes to prototype with paper are [cardboard mechanisms](https://www.pinterest.com/helgangchin/paper-mechanisms/) which move and change. 

<img src="https://dysonthedesigner.weebly.com/uploads/2/6/3/9/26392736/427342_orig.jpg"  width="200" > Dyson Vacuum cardboard prototypes


### For lab, you will need:

1. Cardboard (start collecting those shipping boxes!)
1. Cutting board
1. Cutting tools
1. Markers
1. Found objects and materials--like bananas--we're not saying that to be funny.


### Deliverables for this lab are: 
1. Sketches/photos of device designs
1. "Looks like" prototypes: show us what how the device should look, feel, sit, weigh, etc.
3. "Works like" prototypes: show us what the device can do
4. "Acts like" prototypes: videos/storyboards/other means of showing how a person would interact with the device
5. Submit these in the lab 4 folder of your class [Github page], either as links or uploaded files. Each group member should post their own copy of the work to their own Lab Hub, even if some of the work is the same for each person in the group.


## Overview
Here are the parts of the assignment

A) [Capacitive Sensing](#part-a)

B) [OLED screen](#part-b) 

C) [Paper Display](#part-c)

D) [Record the interaction](#part-d-record)

## The Report
This readme.md page in your own repository should be edited to include the work you have done. You can delete everything but the headers and the sections between the **stars**. Write the answers to the questions under the starred sentences. 

Include any material that explains what you did in this lab hub folder, and link it in the readme.

Labs are due on Mondays. Make sure this page is linked to on your main class hub page.

### Part A: Capacitive Sensing, a.k.a. Human Banana Interaction

We wanted to introduce you to the [capacitive sensor](https://learn.adafruit.com/adafruit-mpr121-gator) in your kit. It's one of the most flexible input devices we were able to provide. At boot it measures the capacitance on each of the 12 contacts. Whenever that capacitance changes it considers it a user touch. You can attach any conductive material. In your kit you have conductive fabric and copper tape that will work well, but don't limit yourself! In this lab we will use (go?) bananas!

<p float="left">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150" />
<img src="https://cdn-shop.adafruit.com/1200x900/4401-01.jpg" height="150">
<img src="https://post.healthline.com/wp-content/uploads/2020/08/banana-pink-background-thumb-1-732x549.jpg" height="150">
</p>

Plug in the capacitive sensor board with the qwiic connector. Connect your banana's with either the copper tape or the alligator clips (the clips work better). make sure to install the requirements from `requirements.txt`

![](https://media.discordapp.net/attachments/679721816318803975/823299613812719666/PXL_20210321_205742253.jpg?width=1518&height=1139)

I've connected my banana's* to pads 6 and 10. When you run the code and touch a banana the terminal will print out the following

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python cap_test.py 
Banana 10 touched!
Banana 6 touched!
```

*\*Some students have noted that their banana's look noticeably different from the ones presented in this demo. We firmly reject the accusation that these are not in fact banana's but Twizzlers™. Due to the challenges of remote teaching we cannot debug banana's at this time. We suggest you bring these issues up with the university or your local produce representative*

I tried the capacitor with a glass of water:

<img src="https://github.com/hgimonet/sp2021_IDD_Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/capacitor.jpg" height="400">

### Part B: OLED screen

We just received some of the small oled screens that we had coped to include in your kit. If you want one feel free to pop into the lab and get one. These don't have colors like the one on the pi but you can move it around on a cable making for more flexible interface design. The way you program this display is almost identical to the pi display. Take a look at `oled_test.py` and some more of the [Adafruit examples](https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/tree/master/examples).

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/6/1/3/5/17153-SparkFun_Qwiic_OLED_Display__0.91_in__128x32_-01.jpg" height="200" />
<img src="https://cdn.discordapp.com/attachments/679466987314741338/823354087105101854/PXL_20210322_003033073.jpg" height="200">
</p>

Since I cannot make it to Roosevelt island to pick up the OLED, I tried hooking up another (jankier) 1602 LCD display, by following [this tutorial](https://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/). 
I was able to daisy-chain the LED using the STEMMA QT cables.

<img src="https://github.com/hgimonet/sp2021_IDD_Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/LED_setup.jpg" width="600" />

I wrote a quick command line interface to write on the LED screen [here](https://github.com/hgimonet/sp2021_IDD_Interactive-Lab-Hub/blob/Spring2021/Lab%204/LCD_driver_LCD_write.py).

### Part C: Paper Display

[comment]: <> (Here is an Pi with a paper faceplate on it to turn it into a display:)

[comment]: <> (<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/paper_if.png?raw=true"  width="250"/>)


[comment]: <> (This is fine, but it can be a bit difficult to lay out a great and user friendly display within the constraints of the Pi. Also, it really only works for applications where people can come and stand over the Pi, or where you can mount the Pi to the wall.)

[comment]: <> (Here is another prototype for a paper display:)

[comment]: <> (<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/b_box.png?raw=true"  width="250"/>)

[comment]: <> (It holds a pi and usb power supply, and provides a front stage on which to put writing, graphics, LEDs, buttons or displays.)

[comment]: <> (This design can be made by scoring a long strip of corrugated cardboard of width X, with the following measurements:)

[comment]: <> (| Y height of box <br> <sub><sup>- thickness of cardboard</sup></sub> | Z  depth of box <br><sub><sup>- thickness of cardboard</sup></sub> | Y height of box  | Z  depth of box | H height of faceplate <br><sub><sup>* * * * * &#40;don't make this too short&#41; * * * * *</sup></sub>|)

[comment]: <> (| --- | --- | --- | --- | --- | )

[comment]: <> (Fold the first flap of the strip so that it sits flush against the back of the face plate, and tape, velcro or hot glue it in place. This will make a H x X interface, with a box of Z x X footprint &#40;which you can adapt to the things you want to put in the box&#41; and a height Y in the back. )

[comment]: <> (Here is an example:)

[comment]: <> (<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/horoscope.png?raw=true"  width="250"/>)


[comment]: <> (Make a paper display for your project that communicates the state of the Pi and a sensor. Ideally you should design it so that you can slide the Pi out to work on the circuit or programming, and then slide it back in and reattach a few wires to be back in operation.)

#### Preliminary Sketches

Make a paper display for your project that communicates the state of the Pi and a sensor. Ideally you should design it so that you can slide the Pi out to work on the circuit or programming, and then slide it back in and reattach a few wires to be back in operation.
 
**a. Document the design for your paper display.** (e.g. if you had to make it again from scratch, what information would you need?). Include interim iterations (or at least tell us about them).

For the sketches, see below:

<img src="https://github.com/hgimonet/sp2021_IDD_Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/smart_bowl_sketches.png" width="700" />

I made a cartboard shape with holes for the janky OLED display:
<p float="center">
<img src="https://github.com/hgimonet/sp2021_IDD_Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/Project%20-%20Drawing%2025600176714355697268.png" width="400" />
<img src="https://github.com/hgimonet/sp2021_IDD_Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/looks_like_prototype.jpg" width="400" />
<img src="https://github.com/hgimonet/sp2021_IDD_Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/box.jpg" width="800" />
</p>

To make the box, I started with the base, and measured all the sides so I could make the sides of the box. Each face of the box had extra tabs that were folded and either taped or stappled to the inside of the ajunct face. One thing I should have done _before_ stappling was punching the holes out for the power supply... I managed to figure it out eventually. I then measured the size of the OLED, and cut a hole in the front face so I could fit the OLED in snuggly. I also cut two thin holes at the top of the box to pass through some aluminum foil for the capacitive reset button. The aluminum foil was then attached tot he capacitor, which I taped to the box to avoid rattling. 

**b. Make a video of your paper display in action.**

The working prototype is available here:

[![](http://img.youtube.com/vi/LUEwM_ZiFIg/0.jpg)](http://www.youtube.com/watch?v=LUEwM_ZiFIg "")

This prototype shows what the device would act like, as well as a general concept of form for the device.

**c. Explain the rationale for the design.** (e.g. Does it need to be a certain size or form or need to be able to be seen from a certain distance?)

The cartboard box I made in one go, as I had a general idea of the shape and size I was going for. I knew I wanted the plane with the OLED to be slanted so that a human could read the screen easily if the device was either on the floor or a low piece of furniture. The size was partly due to the fact it needed to be able to house the pi, and also because I didn't want something so small that you lose it -- idealy the display would be larger as well. I thought having something about the size of a dog bowl would be approriate. 

### Part D: Materiality

[comment]: <> (**Open Ended**: We are putting very few constraints on this part but we want you to get creative.)

[comment]: <> (Design a system with the Pi and anything from your kit with a focus on form, and materiality. The "stuff" that enclose the system should be informed by the desired interaction. What would a computer made of rocks be like? How would an ipod made of grass behave? Would a roomba made of gold clean your floor any differently?)

[comment]: <> (**a. document the material prototype.** Include candidates that were considered even if they were set aside later.)

I wanted to try my hand at working with plastic, which I thought would be appropriate since the final device would have to be waterproof. I learned that plastic is much much harder to work with. Because of that, I figured I could leverage the original corugated qualtity and shape of the plastic, and only modify it to fit the display and button. Because the shape was not oriented towards the top, I thought it could make a good wall display.

<p float="left">
<img src="https://github.com/hgimonet/sp2021_IDD_Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/20210405_083538.jpg" height="600" />
<img src="https://github.com/hgimonet/sp2021_IDD_Interactive-Lab-Hub/blob/Spring2021/Lab%204/imgs/20210405_083551.jpg" height="600" />
</p>

I also made a third iteration with an upcycled plastic takout bowl and a catboard box - I was still too chicken to try it with water, but theoratically it would be safe to use. The video is bellow:

[![](http://img.youtube.com/vi/vGvevt46Yco/0.jpg)](http://www.youtube.com/watch?v=vGvevt46Yco "")


For the prototype, I also considered home-made drying play dough, but realized that the things I make out  of that shrink, so I wouldn't be able to fit it to the oled display.

I also really wanted to make the bowl design, but I couldnt bring myself to make a functional one with pi, since it might get wet. Waterproofness would obviously be a major material requirement for the final design, wether in the bowl or display shape.

I think final materials could include porcelain and rough plastic.

[comment]: <> (**b. explain the selection.**)

