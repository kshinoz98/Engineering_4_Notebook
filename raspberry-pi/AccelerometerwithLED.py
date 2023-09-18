import adafruit_mpu6050                     #[2-5] Import necessary libraries
import busio
import board                        
import time
import digitalio
sda_pin = board.GP14                        #[6-9] Set up SDA and SCL pints
scl_pin = board.GP15
i2c = busio.I2C(scl_pin,sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)
led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT

while True: 
    if mpu.acceleration[1] > 8 or mpu.acceleration[0] > 8 or mpu.acceleration[1] < -8 or mpu.acceleration[0] < -8:                                 #[11-15] Print necessary aspects of acceleration
        print(f"x={mpu.acceleration[0]}.")          
        print(f"y={mpu.acceleration[1]}.")
        print(f"z={mpu.acceleration[2]}.\n")
        led.value = True
        time.sleep(.25)