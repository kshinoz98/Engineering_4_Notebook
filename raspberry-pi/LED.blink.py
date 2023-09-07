# type: ignore
import board
import time
import digitalio
led = digitalio.DigitalInOut(board.GP0)
led2 = digitalio.DigitalInOut(board.GP1)
led.direction = digitalio.Direction.OUTPUT
led2.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    led2.value = False
    time.sleep(1)
    led.value = False
    led2.value = True
    time.sleep(1)

