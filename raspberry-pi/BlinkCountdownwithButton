# type: ignore
import board                                    #[2-4] Import neccesary libraries
import time
import digitalio
redLED = digitalio.DigitalInOut(board.GP0)      #[5-11] Setup LEDs and Button
greenLED = digitalio.DigitalInOut(board.GP2)
button = digitalio.DigitalInOut(board.GP3)
redLED.direction = digitalio.Direction.OUTPUT
greenLED.direction = digitalio.Direction.OUTPUT
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

count = 0                  

while True:
    if button.value == False:                  #[16-17] If the button is pressed, start the countdown
        count = 10
    while count > 0:                           #[18-24] Count down and blink red LED if the time is greater than 0
        print(count)
        redLED.value = True   
        count = count - 1
        time.sleep(.5)
        redLED.value = False
        time.sleep(.5)
        if button.value == False:              #[25-27] If the button is pressed during the countdown, stop the countdown and print abort
            button.value = 3
            print("aborted")
        if count == 0:                         #[28-31] If the countdown is 0, print launch, and turn on the green LED
            print("launch")
            greenLED.value = True
            time.sleep(5)                       #Keeps the board alive
            greenLED.value = False
            print("launched")