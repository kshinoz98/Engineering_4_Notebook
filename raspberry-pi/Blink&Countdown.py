# type: ignore
import board                                    #[2-4] Import neccesary libraries
import time
import digitalio
redLED = digitalio.DigitalInOut(board.GP0)      #[5-8] Setup LEDs
greenLED = digitalio.DigitalInOut(board.GP2)
led.direction = digitalio.Direction.OUTPUT
led2.direction = digitalio.Direction.OUTPUT

count = 10                                      #Set the time to 10 seconds

while count > 0:                              #[12-18] Count down and blink red LED if the time is greater than 0
    print(count)
    redLED.value = True   
    count = count - 1
    time.sleep(.5)
    redLED.value = False
    time.sleep(.5)
    if count == 0:                              #[19-21] If the countdown is 0, print launch, and turn on the green LED
        print("launch")
        greenLED.value = True
while True:                                     #[22-24] Keeps the board alive
    time.sleep(100)
