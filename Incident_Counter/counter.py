from time import sleep
from datetime import datetime
import display_alt

#!/usr/bin/env python3
char = "null"
coolDown = False
print("booted")
display_alt.setDisplay(000)

def test():
    while true:
        print("I'm running")

test()

def Counter():
    global char

    rf = open('data2.txt', 'r') 
    rf.seek(0)
    char = str(rf.read(3))

    print(char)
    print("")
    if char.isdigit():
        print(char)
        print(type(char))
        char = int(char)
        print(type(char))
        char += 1
        print(char)
        
        rf.close()
        with open('data2.txt', 'w') as f:
            f.write(str(char))
        display_alt.setDisplay(char)
    else:
        print("ERROR: Day count is not an integer")

def LogDate():
    global char

    DateNTime = datetime.now()
    startCount = (int(char) - 1)
    endCount = int(char)

    log = str("{}: from {} days to {} \n".format(DateNTime, startCount, endCount))
    
    with open('date_log.txt', 'a') as f:
        f.write(log)

while True:
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    #print(time)
    if time == "07:40:00" and coolDown == False:
        Counter()
        LogDate()
        coolDown = True
        continue
    elif time == "07:42:00" and coolDown == True:
        coolDown = False
    else:
        continue