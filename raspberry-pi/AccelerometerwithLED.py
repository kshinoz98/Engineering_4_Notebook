#type:ignore
import adafruit_mpu6050                     #[2-6] Import necessary libraries
import busio
import board                        
import time
import digitalio
sda_pin = board.GP14                        #[7-12] Set up accelerometer, LED, SDA and SCl pins.
scl_pin = board.GP15
i2c = busio.I2C(scl_pin,sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)
led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT

while True:                                 #[14-17] If the accelerometer is tilted more than 90 degrees, turn the light on
    if mpu.acceleration[2] < 1:      
        led.value = True
        time.sleep(.25)
    else:                                   #[18-19] If the accelerometer is not tilted more than 90 degrees, turn the light off
        led.value = False