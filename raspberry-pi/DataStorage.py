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
led = digitalio.DigitalInOut(board.GP2)
led.direction = digitalio.Direction.OUTPUT

with open("/data.csv", "a") as datalog:
    while True:
            t = time.monotonic()
            x_accel = mpu.acceleration[0]
            y_accel = mpu.acceleration[1]
            z_accel = mpu.acceleration[2]
            if z_accel < .5:
                led = True      
                tilt = "Tilted"
            else:
                led = False
                tilt = "Untilted"
            datalog.write(f"{t},{x_accel},{y_accel},{z_accel},{tilt}\n")
            led = True
            datalog.flush()
            time.sleep(0.25)
            led = False