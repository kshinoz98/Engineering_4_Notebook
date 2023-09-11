# type: ignore
import board                                    #[2-4] Import neccesary libraries
import time
import digitalio
import pwmio
from adafruit_motor import servo
pwm_servo = pwmio.PWMOut(board.GP6, duty_cycle=2 ** 15, frequency=50)
redLED = digitalio.DigitalInOut(board.GP0)      #[5-8] Setup LEDs
greenLED = digitalio.DigitalInOut(board.GP2)
button = digitalio.DigitalInOut(board.GP3)
redLED.direction = digitalio.Direction.OUTPUT
greenLED.direction = digitalio.Direction.OUTPUT
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)

servo1.angle = 0
count = 0                                      #Set the time to 10 seconds

while True:
    if button.value == False:
        count = 10
    while count > 0:                                #[12-18] Count down and blink red LED if the time is greater than 0
        print(count)
        redLED.value = True   
        count = count - 1
        time.sleep(.5)
        redLED.value = False
        time.sleep(.5)
        if count == 0:                              #[19-21] If the countdown is 0, print launch, and turn on the green LED
            print("launch")
            greenLED.value = True
            servo1.angle = 90
            time.sleep(5)                           #Keeps the board alive
            greenLED.value = False
            print("launched")
            servo1.angle = 0

