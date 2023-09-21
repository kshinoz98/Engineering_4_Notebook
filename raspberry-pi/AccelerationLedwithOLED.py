#type:ignore
import adafruit_mpu6050                             #[2-10] Import necessary libraries
import busio
import board                        
import time
import digitalio
import terminalio
import displayio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

displayio.release_displays()                        #[12-18] Set up SDA, SCL and display bus
sda_pin = board.GP14                        
scl_pin = board.GP15
i2c = busio.I2C(scl_pin,sda_pin)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP3)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)   #Intialize OLED

led = digitalio.DigitalInOut(board.GP0)             #[21-22] Set up LED
led.direction = digitalio.Direction.OUTPUT

splash = displayio.Group()                          #[24-28] Set up Splash for OLED display
title = "ANGULAR VELOCITY"
text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
splash.append(text_area)
display.show(splash)

while True:                                         #[30-33] If the accelerometer is tilted more than 90 degrees, turn the light on and print CRASSSSSHHHH@!!!!!!
    if mpu.acceleration[2] < 1:      
        led.value = True
        text_area.text = "CRASSSSSHHHH@!!!!!!"
    else:                                           #[34-36] Print the Gyro values from the accelerometer
        led.value = False
        text_area.text = f"x={mpu.gyro[0]:.3f}\ny={mpu.gyro[1]:.3f}\nz={mpu.gyro[2]:.3f}\n"