import math

def calcTri(x1,y1,x2,y2,x3,y3):
    try: 
        Triarea =  abs((x1(y2-y3) + x2(y3-y1) + x3(y1-y2))*.5)
        return Triarea
    except:
         print("one of those points don't work")


PUTT = input("Enter your points in form (x1,y1,x2,y2,x3,y3):")
PUTT = PUTT.split(",")
try:
    x1 = float(PUTT[0])
    y1 = float(PUTT[1])
    x2 = float(PUTT[2])
    y2 = float(PUTT[3])
    x3 = float(PUTT[4])
    y3 = float(PUTT[5])
    calcTri(x1,y1,x2,y2,x3,y3)
    print("The area of the triangle with vertices ({x1},{y1}), ({x2},{y2}), ({x3},{y3}) is {Triarea} square km.")
except:
    print("one of those points don't work")