#type:ignore
import time                                             #[2-11] Import necessary libraries and clear the pins for the display
import board
import busio
import displayio
import terminalio
import adafruit_displayio_ssd1306
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle
from adafruit_display_text import label

displayio.release_displays()                            #[13-18] Set up OLED Display
sda_pin = board.GP14                                    
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin) 
display_bus = displayio.I2CDisplay(i2c, device_address = 0x3d, reset = board.GP0) 
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

def calcandgraphtri(x1,y1,x2,y2,x3,y3):                 #[20-39] Create a function which calculates the area of a triangle from three coords and graphs it.
    try:
        area = abs((x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))*.5)
        splash = displayio.Group()
        print(f"\nThe area of the triangle with the coordinates ({x1},{y1}), ({x2},{y2}), ({x3},{y3}) is {area} km squared")
        hline = Line(0,32,128,32, color=0xFFFF00)
        splash.append(hline)
        vline = Line(64,64,64,0, color=0xFFFF00)
        splash.append(vline)
        triangle = Triangle(int(x1+64), int(-y1+32), int(x2+64), int(-y2+32), int(x3+64), int(-y3+32), outline=0xFFFF00)
        splash.append(triangle)
        circle = Circle(64, 32, 3, outline=0xFFFF00)
        splash.append(circle)  
        title = f"Area: {area}"
        text_area = label.Label(terminalio.FONT, text = title, color = 0xFFFF00, x = 5, y= 5)
        splash.append(text_area)
        display.show(splash)          
        return area
    except:
        print("These points are invalid, try again")

while True:                                             #[41-49] Take user-inputted points and split them into an array then define them as points
    INPUTT = input("Enter your points in form x1,y1,x2,y2,x3,y3:")
    PUTT = INPUTT.split(",")
    x1 = float(PUTT[0])
    y1 = float(PUTT[1])
    x2 = float(PUTT[2])
    y2 = float(PUTT[3])
    x3 = float(PUTT[4])
    y3 = float(PUTT[5])
    areaA = calcandgraphtri(x1,y1,x2,y2,x3,y3)         #Run the previosly defined function to calculate the area and graph it on an OLED
    if areaA == 0:                                     #[51-54] Print the results on the serial moniter, if the triangle doesn't exist then restart the while true loop
        continue
    else:
        print(f"The area of the triangle with vertices ({x1},{y1}), ({x2},{y2}), ({x3},{y3}) is {areaA} square km.")