# Observant Systems

For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the
environment of the Pi, like the Boat Detector we mentioned in lecture. Your **observant device** could, for example,
count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms need
to be aware of.

In Lab 5 part 1, we focus on detecting and sense-making.

In Lab 5 part 2, we'll incorporate interactive responses.

## Prep

1. Pull the new Github Repo.
2. Read about [OpenCV](https://opencv.org/about/).
3. Read Belloti, et
   al's [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf)

### For the lab, you will need:

1. Raspberry Pi
1. Raspberry Pi Camera (2.1)
1. Microphone (if you want speech or sound input)
1. Webcam (if you want to be able to locate the camera more flexibly than the Pi Camera)

### Deliverables for this lab are:

1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.

## Overview

Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are
the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

## Part 1

### Part A

### Play with different sense-making algorithms.

Befor you get started connect the RaspberryPi Camera
V2. [The Pi hut has a great explanation on how to do that](https://thepihut.com/blogs/raspberry-pi-tutorials/16021420-how-to-install-use-the-raspberry-pi-camera)
.

#### OpenCV

A more traditional to extract information out of images is provided with OpenCV. The RPI image provided to you comes
with an optimized installation that can be accessed through python.

Additionally, we also included 4 standard OpenCV examples. These examples include contour(blob) detection, face
detection with the ``Haarcascade``, flow detection(a type of keypoint tracking), and standard object detection with
the [Yolo](https://pjreddie.com/darknet/yolo/) darknet.

Most examples can be run with a screen (I.e. VNC or ssh -X or with an HDMI monitor), or with just the terminal. The
examples are separated out into different folders. Each folder contains a ```HowToUse.md``` file, which explains how to
run the python example.

```shell
pi@ixe00:~/openCV-examples $ tree -l
.
├── contours-detection
│   ├── contours.py
│   └── HowToUse.md
├── data
│   ├── slow_traffic_small.mp4
│   └── test.jpg
├── face-detection
│   ├── face-detection.py
│   ├── faces_detected.jpg
│   ├── haarcascade_eye_tree_eyeglasses.xml
│   ├── haarcascade_eye.xml
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_frontalface_default.xml
│   └── HowToUse.md
├── flow-detection
│   ├── flow.png
│   ├── HowToUse.md
│   └── optical_flow.py
└── object-detection
    ├── detected_out.jpg
    ├── detect.py
    ├── frozen_inference_graph.pb
    ├── HowToUse.md
    └── ssd_mobilenet_v2_coco_2018_03_29.pbtxt
```

#### Filtering, FFTs, and Time Series data.

Additional filtering and analysis can be done on the sensors that were provided in the kit. For example, running a Fast
Fourier Transform over the IMU data stream could create a simple activity classifier between walking, running, and
standing.

Using the set up from the [Lab 3 demo](https://github.com/FAR-Lab/Interactive-Lab-Hub/tree/Spring2021/Lab%203/demo) and
the accelerometer, try the following:

**1. Set up threshold detection** Can you identify when a signal goes above certain fixed values?

**2. Set up averaging** Can you average your signal in N-sample blocks? N-sample running average?

**3. Set up peak detection** Can you identify when your signal reaches a peak and then goes down?

Include links to your code here, and put the code for these in your repo--they will come in handy later.

#### Teachable Machines (beta, optional)

Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) might look very simple. However, its
simplicity is very useful for experimenting with the capabilities of this technology.

You can train a Model on your browser, experiment with its performance, and then port it to the Raspberry Pi to do even
its task on the device.

Here is Adafruit's directions on using Raspberry Pi and the Pi camera with Teachable Machines:

1. [Setup](https://learn.adafruit.com/teachable-machine-raspberry-pi-tensorflow-camera/raspberry-pi-setup)
2. Install Tensorflow:
   Like [this](https://learn.adafruit.com/running-tensorflow-lite-on-the-raspberry-pi-4/tensorflow-lite-2-setup), but
   use
   this [pre-built binary](https://github.com/bitsy-ai/tensorflow-arm-bin/) [the file](https://github.com/bitsy-ai/tensorflow-arm-bin/releases/download/v2.4.0/tensorflow-2.4.0-cp37-none-linux_armv7l.whl)
   for Tensorflow, it will speed things up a lot.
3. [Collect data and train models using the PiCam](https://learn.adafruit.com/teachable-machine-raspberry-pi-tensorflow-camera/training)
4. [Export and run trained models on the Pi](https://learn.adafruit.com/teachable-machine-raspberry-pi-tensorflow-camera/transferring-to-the-pi)

Alternative less steps option is [here](https://github.com/FAR-Lab/TensorflowonThePi).

#### PyTorch

As a note, the global Python install contains also a PyTorch installation. That can be experimented with as well if you
are so inclined.

### Part B

### Construct a simple interaction.

Pick one of the models you have tried, pick a class of objects, and experiment with prototyping an interaction. This can
be as simple as the boat detector earlier. Try out different interactions outputs and inputs.
**Describe and detail the interaction, as well as your experimentation.**

I tried to make a sleep detector using the eye Haar cascades, but as it turned out, the eye cascade is robust to closing
your eyes.(I had hoped I would be able to exploit a weekness in the detection when the eyes are closed so I could make
an open/closed classification). Tinkering with the eye detection however gave me the idea of using the smile detector as
a proxy for emotion.

I ended up using the face and smile Haar cascades from OpenCV to build a lo-fi emotion detector. My detector looks at
the first face detected, and check whether is detects a smile in the face. I had to tinker with the scale factor and
minimum number of neighbors parameters so that the smile could be detected when the face was further away.

### Part C

### Test the interaction prototype

Now flight test your interactive prototype and **note your observations**:
For example:

1. When does it what it is supposed to do?
1. When does it fail?
1. When it fails, why does it fail?
1. Based on the behavior you have seen, what other scenarios could cause problems?

The smile detection only works when the face is facing the camera. It's really good at detecting smiles, even tentative
ones, and not detecting anything that is a frown. It however can be tricked by grimaces showing teeth -- I hypothesize
the model probably associates teeth with smiles regardless of the shape of the mouth. I think it would work as a really
rough mood detector, but not if users are intent on trying to break the system.

Good Examples:
<p float="left">
<img src="https://github.com/hgimonet/sp2021_IDD_Interactive-Lab-Hub/blob/Spring2021/Lab%205/imgs/Screenshot%202021-04-18%20225328.png" height="200" />
<img src="https://github.com/hgimonet/sp2021_IDD_Interactive-Lab-Hub/blob/Spring2021/Lab%205/imgs/Screenshot%202021-04-18%20225425.png" height="200" />
<img src="https://github.com/hgimonet/sp2021_IDD_Interactive-Lab-Hub/blob/Spring2021/Lab%205/imgs/Screenshot%202021-04-18%20225502.png" height="200">
</p>
Left to right: Close-up smiling, close-up not smiling, far away and smiling

Bad Exmaples:
<p float="left">
<img src="https://github.com/hgimonet/sp2021_IDD_Interactive-Lab-Hub/blob/Spring2021/Lab%205/imgs/Screenshot%202021-04-18%20225633.png" height="200">
<img src="" height="200">
</p>

**Think about someone using the system. Describe how you think this will work.**

1. Are they aware of the uncertainties in the system?
1. How bad would they be impacted by a miss classification?
1. How could change your interactive system to address this?
1. Are there optimizations you can try to do on your sense-making algorithm.

I think the imact on the user would depend on the usage. Since people are generally good at reading faces, anyone
looking at the video-feed would be able to tell if the device is correct or not. However, it's possible that the user is
not, in fact, looking at themselves (maybe they are focusing on other things, like their posture if they are dancing, or
the cash register screen for a cashier.)

I think misclassification is relatively low-risk in most cases, because it's usually not a question of life or death
whether someone is smiling, and also because it would be relatively easy to check by hand. However, the data could be
used against the user (for instance, a shop could reprimand a cashier who is consistently misclassified, even if it's
the device's fault). It would be extremely important in that case to save footage that the classification is based on,
so that it can be check with human eyes.

### Part D

### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**. During
the lecture, we mentioned questions to help characterize a material:

* What can you use X for?
* What is a good environment for X?
* What is a bad environment for X?
* When will X break?
* When it breaks how will X break?
* What are other properties/behaviors of X?
* How does X feel?

**Include a short video demonstrating the answers to these questions.**

I originally thought this could be used to tell people not to frown when they are working. This type of solution would
be handy for people spending a lot of time in front of their computer, since frowning give you wrinkles! It could also
be used as a training device for cashiers or dancers, or anyone who should be able to perform intensive tasks without
frowning.
After testing the system though, I realized this would also be really handy in a camera, to take pictures without the
user having to press a button. If it worked for multiple faces, it could be used to capture the moment where as many
people as possible are looking at the camera and smiling.

My device as is wouldn't work in a crowded environment. It also wouldn't work on face that are not directly looking at 
the camera, which limits the possible use cases. I think any enviromnent with a static user would be okay, since the 
device can be place somewhere facing the user. Any environment where the users would be invested in looking straight 
at the device would work too -- in a personal camera, a photo-booth, or possibly a mirror. 

The way I set it up, the device breaking only happens in the form of misclassification. It definitely breaks when the 
user grimaces, and can also make mistakes when there is more than one face in front of the camera.

The device feels a little strange - I was hoping it would be fun and encouraging, but the boxes around the face and 
mouth are a little off-putting. I think it would make sense to remove the bounding boxes, and simply have textual 
feedback on what is detected. I also tried voice feedback, which I think works well for a use-case where the user is 
not looking at the video as it is taken.


## Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use
iwth a video.
**Include a short video demonstrating the finished result.**

