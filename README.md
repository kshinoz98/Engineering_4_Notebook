# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Launch Pad Countdown](#Launch_Pad_Countdown)
* [Launch Pad Lights](#Launch_Pad_Lights)
* [Launch Pad Lights with Button](#Launch_Pad_Lights_with_Button)
* [Launch Pad Lights with Button and Servo ](#Launch_Pad_Lights_with_Button_and_Servo)
* [Accelerometer](#Accelerometer)
* [Accelerometer with LED and Battery](#Accelerometer_with_LED_and_Battery)
* [Accelerometer with OLED, LED and Battery](#Accelerometer_with_OLED,_LED_and_Battery)

&nbsp;

## Launch Pad Countdown

### Assignment Description

Use the serial moniter on the pico to count down from 10 to a launch

### Evidence 

![Untitled_ Sep 6, 2023 10_46 AM](https://github.com/kshinoz98/Engineering_4_Notebook/assets/113209502/d8c9d4cf-d585-458c-833a-3f2df7ea796e)

### Code

[Something like this](https://github.com/kshinoz98/Engineering_4_Notebook/blob/main/raspberry-pi/Countdown.py)

### Reflection

This assignment was very easy, as it was a repeated loop until the count equals to 0. The hardest part of the assignment was deciding which way to code it was the easiest, which I decided was using a while loop. I had a bit of trouble using VS, specifically getting out of a REPL, but now I know Ctrl + D.

&nbsp;

## Launch Pad Lights

### Assignment Description

Using a Pi pico and the code from launch pad countdown, blink a light every time it counts down and turn on another light when it launches.

### Evidence 

![ezgif-3-644f7e1271](https://github.com/kshinoz98/Engineering_4_Notebook/assets/113209502/b88b7211-b245-441d-a800-0d9a66ea3640)

### Wiring

![IMG_0892](https://github.com/kshinoz98/Engineering_4_Notebook/assets/113209502/ba515912-fdc7-4d9c-b1be-83612152002d)

### Code

[Link to code](https://github.com/kshinoz98/Engineering_4_Notebook/blob/main/raspberry-pi/Blink%26Countdown)

### Reflection

This was a nice refresher on how to wire a LED (220 omh resistor, 5v to GND). I had some trouble with the run button, which seems to have broken since the last assignment, So now I use **Ctrl + s** to upload the code. There was not much difference between this and the last assignment in terms of code, only a few lines of code to set up and turn on and off the LED lights. I did forget about DigitallInOut, but [this site](https://docs.circuitpython.org/en/latest/shared-bindings/digitalio/index.html) just gave me all the code I needed, which helped a lot.

&nbsp;

## Launch Pad Lights with Button

### Assignment Description

Using a Pi pico and building from the code from the previous assignment, use a button to trigger the countdown, blink a light every time it counts down and turn on another light when it launches. I did the additional spicy part that has an abort button as well.

### Evidence 

![ezgif-1-514e74e366](https://github.com/kshinoz98/Engineering_4_Notebook/assets/113209502/19fb9288-165d-4c4d-98ae-45bcbbb879a3)

### Wiring

![IMG_0896](https://github.com/kshinoz98/Engineering_4_Notebook/assets/113209502/81968267-8e90-41ae-9ff9-cdb5314449db)

### Code

[Link to code](https://github.com/kshinoz98/Engineering_4_Notebook/blob/main/raspberry-pi/BlinkCountdownwithButton)

### Reflection

There are so many different ways to do this assignment. I looked at my code, and I looked at Elias' code, and I looked at Graham's code, and they were all radically different(mostly because we used different types of [loops](https://www.simplilearn.com/tutorials/python-tutorial/python-loops)) but they all worked. I choose to use a **while()** loop because that was what I knew the best, and made the button add 10 to the count. I had a slight problem with pull.UP vs pull.DOWN (I switched them and the button was always on) but I fixed that by flipping the logic(after being puzzled for like 10 minutes).

&nbsp;

## Launch Pad Lights with Button and Servo 

### Assignment Description

Using a Pi pico and building from the code from the previous assignment, use a button to trigger the countdown, blink a light every time it counts down and turn on another light when it launches. After 7 seconds, start moving the servo slowly untill it launches.

### Evidence 

![ezgif-5-4ddbf5f32e](https://github.com/kshinoz98/Engineering_4_Notebook/assets/113209502/b993184b-4840-4029-a413-fdee0397bdde)

### Wiring

![IMG_0900](https://github.com/kshinoz98/Engineering_4_Notebook/assets/113209502/20d9c779-b66b-46be-bb21-881f0ebe155e)

### Code

[Link to code](https://github.com/kshinoz98/Engineering_4_Notebook/blob/main/raspberry-pi/BlinkCountButtonServo.py)

### Reflection

This assignment was much harder than the previous assignments. It required a lot more indepth code logic, specifically a for loop, which I had never worked with before. I needed Elias to explain how to repeat a line of code 10 times, because Mr. Miller got mad at me copy and pasting the same line of code 10 times. Aside from that, it was just adding another while loop to my logic to run when the time was less than 3.

&nbsp;

## Accelerometer

### Assignment Description

Find the orientation of a Pico by using an accelerometer and reading the acceleration due to gravity.

### Evidence 

![ezgif-5-b68dc04efc](https://github.com/kshinoz98/Engineering_4_Notebook/assets/113209502/a351c4f9-7247-4c90-8a86-927c183805ff)

### Wiring

![IMG_0902](https://github.com/kshinoz98/Engineering_4_Notebook/assets/113209502/119f78eb-c848-4b0d-8edc-1d7394bee741)

### Code

[Link to code](https://github.com/kshinoz98/Engineering_4_Notebook/blob/main/raspberry-pi/Accelerometer.py)

### Reflection

[I2C](https://www.geeksforgeeks.org/i2c-communication-protocol/) devices are very interesting. Using only two pins, it is possible to communicate with multiple devices, which reduces the complexity of wiring by a factor of how many devices are attached. While this feature is not used in this assignment, I found it really cool when I found out about it, enough to talk about it in the reflection. Also, [F strings](https://www.freecodecamp.org/news/python-f-strings-tutorial-how-to-use-f-strings-for-string-formatting/) are very strange, but Elias helped me out with them, so I think I know enough to use them in the future.

&nbsp;

## Accelerometer

### Assignment Description

Find the orientation of a Pico by using an accelerometer and reading the acceleration due to gravity.

### Evidence 

![ezgif-5-b68dc04efc](https://github.com/kshinoz98/Engineering_4_Notebook/assets/113209502/a351c4f9-7247-4c90-8a86-927c183805ff)

### Wiring

![IMG_0902](https://github.com/kshinoz98/Engineering_4_Notebook/assets/113209502/119f78eb-c848-4b0d-8edc-1d7394bee741)

### Code

[Link to code](https://github.com/kshinoz98/Engineering_4_Notebook/blob/main/raspberry-pi/Accelerometer.py)

### Reflection

[I2C](https://www.geeksforgeeks.org/i2c-communication-protocol/) devices are very interesting. Using only two pins, it is possible to communicate with multiple devices, which reduces the complexity of wiring by a factor of how many devices are attached. While this feature is not used in this assignment, I found it really cool when I found out about it, enough to talk about it in the reflection. Looking back on it, I don't think I would be able to figure out the setup code if I was not given it, as I still do not know what the busio does. Also, [F strings](https://www.freecodecamp.org/news/python-f-strings-tutorial-how-to-use-f-strings-for-string-formatting/) are very strange when you're not used to it, but Elias helped me out with them, so I think I know enough to use them in the future.

&nbsp;

## Accelerometer with LED and Battery

### Assignment Description

Find the orientation of a Pico by using an accelerometer and reading the acceleration due to gravity, turning on a light if the pico is tipped 90 degrees, all powered by battery

### Evidence 

![ezgif-2-23fbeb520b](https://github.com/kshinoz98/Engineering_4_Notebook/assets/113209502/b4a28f7b-09fa-417d-8c4d-5da6ca1e75d3)

### Wiring

![IMG_20230925_103003](https://github.com/kshinoz98/Engineering_4_Notebook/assets/113209502/03de6a68-97df-404b-8b34-931023a8fed5)

### Code

[Link to code](https://github.com/kshinoz98/Engineering_4_Notebook/blob/main/raspberry-pi/AccelerometerwithLED.py)

### Reflection

This application of acceleration due to gravity is very neat, because it is not necessary to measure whether the board is tilted, but whether the z axis acceleration is above a certain level. I had a bit of trouble with that concept, because my original code used the x and y values being higher instead of the z acceleration being lower, but I looked at Matthew's code and realized that wasn't necessary. In the end, this is a bit inaccurate because z acceleration can be caused by just shaking the Pico up and down, but for this application it seems to work. The battery was suprisingly easy to use, but it is a bit scary that if I connect it to the wrong pin, it'll just fry the board.

&nbsp;

## Accelerometer with OLED, LED and Battery

### Assignment Description

Find the orientation of a Pico by using an accelerometer and reading the acceleration due to gravity, print it on an OLED, turning on a light if the pico is tipped 90 degrees, all powered by battery

### Evidence 


### Wiring

![Accelerometer with LED, OLED and Battery Wiring](https://github.com/kshinoz98/Engineering_4_Notebook/assets/113209502/0fa83165-37c6-4a9c-9fd0-f26c2c94ee2a)

### Code

[Link to code](https://github.com/kshinoz98/Engineering_4_Notebook/blob/main/raspberry-pi/AccelerationLedwithOLED.py)

### Reflection

I think that everybody had problems with finding their i2c devices. I still don't know exactly what makes it so hard to do (something to do with the pins being in use?) but the fix for it is simple, just unplug the board, and plug it back in. The other hard thing about using the OLED is the splash, which I don't totally understand(but [here's](https://learn.adafruit.com/adafruit-oled-featherwing/python-usage) a site that somewhat explains it). Other than those things, I was really impressed with the OLED board, it has such a high resolution, and the i2c wiring makes it fast to wire.

&nbsp;

## Beam
### Description
For this assignment we were challenged to create a beam that could support the most amount of weight that we could. It also included several constraints we needed to follow. For example it needed to be 180 mm long and could not use angles greater than 45 degrees.
### Part Link
[Link](https://cvilleschools.onshape.com/documents/612d3b9286e5a0bfa339152e/w/fc81e668b00e0ee0c54c7765/e/e5900d19b5ba4f1918d7debd)
### Part Image
![No.3.png](images/No.3.png)
### Reflection
For this assignment we began by researching beam theory which taught us about point loads and cantilever beams. Using this knowledge we decided to make an I beam with evenly distributed weight. Because of the rule about angles we decided to use Chamfers on the edges which made the angles the right amount of degrees. We also used a loft so that the weight could be distributed better. We owe a lot of thanks to [this website](https://engineering.stackexchange.com/questions/50258/whats-the-best-shape-solid-of-revolution-for-a-cantilever-beam-to-carry-a-poi) for helping us learn about cantilever beams and showing us that the I beam is the best option.

## FEA part 3
### Description
For this part of the assignment we simulated our beam using the onshape simulation to show the deflection and highest stress point.
### Evidence

![No85assembly](https://github.com/kshinoz98/Engineering_4_Notebook/assets/113209502/b31ad806-df4d-47d3-8630-4276b2e7420a)
![No85assembly1](https://github.com/kshinoz98/Engineering_4_Notebook/assets/113209502/3c20a1a1-5155-4274-b6b5-0875704049b4)

### Reflection

Using the analysis that the FEA provided, we quickly tested multiple beam designs(Maybe this wasn't what we were supposed to do, but we made multiple beams and then picked the best one). First we started with a basic I-Beam, but decided not to use that one because the stress point was too concentrated on the back of the beam. For a little bit, we tried an X-Beam design, but that design added no benefits and had worse usage of the PLA. Finally, we tested a tapered I-Beam, which seemed to be the best, not only because the stress was spread out, but because the stress point was adjustable. Thanks to FEA simulation, we were able to tune the stress point of the beam. There was something that we were missing, but we didn't notice that until the next assignment(We bonded the beam wrong to the block in the simulation, so that the results were wrong). Actually, the point on the top where the beam connected to the block actually had the most stress on it. In the next iteration, we will put more support on the back so it will distribute the stress more evenly across the face of the block. I was thinking of adding a fillet there and pushing the overall distribution towards the tip to reduce the stress.

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link

[Hyperlink text](http://www.google.com)      

### Test Image

![Picture Name Here](images/images.jpg)  

### Test GIF

![Picture Name Here](images/200w.gif)  
