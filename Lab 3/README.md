# You're a wizard, Hortense

<img src="https://pbs.twimg.com/media/Cen7qkHWIAAdKsB.jpg" height="400">

In this lab, we want you to practice wizarding an interactive device as discussed in class. We will focus on audio as the main modality for interaction but there is no reason these general techniques can't extend to video, haptics or other interactive mechanisms. In fact, you are welcome to add those to your project if they enhance your design.


## Text to Speech and Speech to Text

In the home directory of your Pi there is a folder called `text2speech` containing some shell scripts.

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav

```

you can run these examples by typing 
`./espeakdeom.sh`. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts

```

You can also play audio files directly with `aplay filename`.

After looking through this folder do the same for the `speech2text` folder. In particular, look at `test_words.py` and make sure you understand how the vocab is defined. Then try `./vosk_demo_mic.sh`

## Serving Pages

In Lab 1 we served a webpage with flask. In this lab you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/$ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to [http://ixe00.local:5000]()


## Demo

In the [demo directory](./demo), you will find an example wizard of oz project you may use as a template. **You do not have to** feel free to get creative. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser. You can control what system says from the controller as well.

## Optional

There is an included [dspeech](.dspeech) demo that uses [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) for speech to text. If you're interested in trying it out we suggest you create a seperarate virutalenv. 



# Lab 3 Part 2

Create a system that runs on the Raspberry Pi that takes in one or more sensors and requires participants to speak to it. Document how the system works and include videos of both the system and the controller.

## Prep for Part 2

1. Sketch ideas for what you'll work on in lab on Wednesday.

<img src="https://github.com/hgimonet/sp2021_IDD_Interactive-Lab-Hub/blob/Spring2021/Lab%203/sketch.jpg" height="500">

Second idea is a memory game where each player adds a new word, and whoever forget the entire sequence looses!

## Share your idea sketches with Zoom Room mates and get feedback

*what was the feedback? Who did it come from?*

Snigdah liked the idea of the memory game, but was concerned about the computer always winning! We figured that the computer could fail to recognize a word, and that that could be a loss.

I actually pivoted midway through lab, because I wanted to work on something a little more exciting, and hearing about other people's projects made me more daring. My next concept is a virtual dog that you can do tricks with!

<img src="https://github.com/hgimonet/sp2021_IDD_Interactive-Lab-Hub/blob/Spring2021/Lab%203/Wizard_Screenshot.png" width="400">

I discussed with my husband (without telling him about the wizarding bit), and he mentioned that the dog could bark when it feels ignored or happy.

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

The system uses
- a Raspberry Pi
- a TFT screen
- a microphone
- an audio player
- a MPU6050 accelerometer

<img src="https://github.com/hgimonet/sp2021_IDD_Interactive-Lab-Hub/blob/Spring2021/Lab%203/setup.jpg" width="400">

The virtual pup is made of sprites I borrowed from [a game mod forum](https://community.playstarbound.com/threads/fluffy-dogs-other-alternative-dog-sprites-update-8-pug-time.109948/). I generated looping frames in [wizard/pup.py] for all the pup's possible reactions. In [wizard/app.py], I have a wizard of oz setup so that I can bark, as well as change the pup's actions displayed on the TFT screen. I am able to also record the actor's speech to find commands for the pup to follow. The user can also pet or wave at the dog with the accelerometer.

The wizard setup can be seen below:

<img src="https://github.com/hgimonet/sp2021_IDD_Interactive-Lab-Hub/blob/Spring2021/Lab%203/Wizard_Screenshot.png" width="400">

The demo is below:
[![](http://img.youtube.com/vi/BM8UjBPzM5o/0.jpg)](http://www.youtube.com/watch?v=BM8UjBPzM5o "Virtual Pup")

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Answer the following:

### What worked well about the system and what didn't?

I wasn't able to make the animations loop infinitely, so the pup is frozen during most of the interaction. I found there are many more things the actors though to try in terms of interactions with the pup (other tricks like paw), just as some interactions I though would be obvious (like calling the dog) were not to my actors. It seems the affordances aren't super clear here.

### What worked well about the controller and what didn't?

The controller actually worked pretty well for what I was aiming for.

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

Definitely incorporate more possible interactions, and find a way to signal what is possible? One of my users said this felt like a voice-controlled tamachochi -- I think I want to push that further - can I add feeding? How do I prompt my used to pet the dog with the accelerometer?

### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

My user definitely had different preconceptions about what they could or couldn't do with the virtual pup; I want to try prompting different ways, and observe what users do when the encounter something voice-based, where you really don't have a clear set of possible instructions. 

In terms of modalities, I think it would be great for the user to be able to personalize their dog as well - maybe they can select a dog and a background? Are people more adventurous or excited when they customized the device?
