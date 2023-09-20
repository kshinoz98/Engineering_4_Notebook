# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Raspberry_Pi_Assignment_Template](#raspberry_pi_assignment_template)
* [Onshape_Assignment_Template](#onshape_assignment_template)

&nbsp;

## Raspberry_Pi_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Evidence 

Pictures / Gifs of your work should go here. You need to communicate what your thing does. 

### Wiring

This may not be applicable to all assignments. Anything where you wire something up, include the wiring diagram here. The diagram should be clear enough that I can recreate the wiring from scratch. 

### Code

[Something like this]()

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

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

This assignment was easy, but a nice refresher on how to use a LED (220 omh resistor). There was not much difference between this and the last assignment in terms of code, only a few lines of code to set up and turn on and off the lights. I had some trouble with the run button, which seems to have broken since the last assignment.

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

This assignment was not very hard, as wiring and coding a button is not too difficult. The only usually hard part is remembering to set up a button, and that was given to us in the assignment. I did have a slight problem with pull.UP vs pull.DOWN (I switched them and the button was always on) but I fixed that by flipping the logic. 

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

Find the orientation of a Pico by using an accelerometer and reading the acceration due to gravity.

### Evidence 

![ezgif-5-b68dc04efc](https://github.com/kshinoz98/Engineering_4_Notebook/assets/113209502/a351c4f9-7247-4c90-8a86-927c183805ff)

### Wiring

![IMG_0902](https://github.com/kshinoz98/Engineering_4_Notebook/assets/113209502/119f78eb-c848-4b0d-8edc-1d7394bee741)

### Code

[Link to code](https://github.com/kshinoz98/Engineering_4_Notebook/blob/main/raspberry-pi/Accelerometer.py)

### Reflection

This assignment was actually very neat. The idea of finding position based on acceleration due to gravity is very cool, and the accelerometer is very easy to use. 

&nbsp;



## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link

[Hyperlink text](http://www.google.com)      

### Test Image

![Picture Name Here](images/images.jpg)  

### Test GIF

![Picture Name Here](images/200w.gif)  
