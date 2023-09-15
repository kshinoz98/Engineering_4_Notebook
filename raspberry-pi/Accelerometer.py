# type: ignore
import adafruit_mpu6050
import busio
import board                        
import time
sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(GP15,GP14)
mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    print(mpu.acceleration)
    time.sleep(.05)