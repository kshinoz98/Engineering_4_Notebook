# type: ignore
import time
import board

count = 10

while count > 0:
    time.sleep(1)
    print(count)
    count = count - 1
else:
    time.sleep(1)
    print("lauch")