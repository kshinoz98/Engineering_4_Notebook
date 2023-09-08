# type: ignore
import time         #[1-2] Import neccesary libraries
import board

count = 10          # Set the time to 10 seconds

while count > 0:    #[7-11] Count down and print if the time is greater than 0
    time.sleep(1)
    print(count)
    count = count - 1
else:
    time.sleep(1)   #[12-13] If the time is 0, print launch
    print("lauch")