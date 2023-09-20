import adafruit_mpu6050                     #[2-5] Import necessary libraries
import busio
import board                        
import time
import digitalio
import terminalio
import displayio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

displayio.release_displays()
sda_pin = board.GP14                        #[6-11] Set up accelerometer, LED, SDA and SCl pins.
scl_pin = board.GP15
i2c = busio.I2C(scl_pin,sda_pin)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP3)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)
led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT
splash = displayio.Group()
title = "ANGULAR VELOCITY"
text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
splash.append(text_area)
display.show(splash)

while True:                                 #[13-16] If the accelerometer is tilted more than 90 degrees, turn the light on
    if mpu.acceleration[2] < 1:      
        led.value = True
        time.sleep(.25)
    else:                                   #[17-18] If the accelerometer is not tilted more than 90 degrees, turn the light off
        led.value = False