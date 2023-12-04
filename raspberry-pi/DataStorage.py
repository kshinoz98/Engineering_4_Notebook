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
printed = False

while True:                                 #[15-25]If the accererometer is tilted, then turn on the light
    t = time.monotonic()
    x_accel = mpu.acceleration[0]
    y_accel = mpu.acceleration[1]
    z_accel = mpu.acceleration[2]
    if z_accel < .5:
        led.value = True     
        tilt = "Tilted"
    else:
        led.value = False
        tilt = "Untilted"
    try:                                   #[26-33]If the Pico is in data mode, save the time; x, y, and z accel; and if the servo is tilted
        with open("/data.csv", "a") as datalog:
            datalog.write(f"{t},{x_accel},{y_accel},{z_accel},{tilt}\n")
            datalog.flush()
    except:
        if printed == False:
            print("data not open")
            printed = True
    led.value = True
    time.sleep(0.25)
    led.value = False