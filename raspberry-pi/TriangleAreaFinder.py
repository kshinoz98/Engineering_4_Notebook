import math                                                         #Import Math Library

def calcTri(x1,y1,x2,y2,x3,y3):                                     #[3-7] Define a function which calulates the area of a triangle from 3 sets of coords
    try: 
        Triarea = abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))*.5
        return Triarea
    except:
         print("that's not a triangle")                            #If the points do not form a triangle then print error message

while True:
    INPUTT = input("Enter your points in form x1,y1,x2,y2,x3,y3:") #[11-19] Take the user input and split it into coords
    PUTT = INPUTT.split(",")
    try:
        x1 = float(PUTT[0])
        y1 = float(PUTT[1])
        x2 = float(PUTT[2])
        y2 = float(PUTT[3])
        x3 = float(PUTT[4])
        y3 = float(PUTT[5])
        Area = calcTri(x1,y1,x2,y2,x3,y3)                           #Call the function to calculate the area of the triangle
        print(f"The area of the triangle with vertices ({x1},{y1}), ({x2},{y2}), ({x3},{y3}) is {Area} square km.") #Print the area of the triangle
    except:                                                         #If the points are not valid then print error message
        print("These points are not a valid triangle. Please try again, and make sure you are using the x1,y1,x2,y2,x3,y3 syntax")  