from time import sleep
from datetime import datetime, date
import calendar
import display_alt

char = "null"
coolDown = False
countWeekends = True

def counter():
    global char

    rf = open('data2.txt', 'r') 
    rf.seek(0)
    char = str(rf.read(3))

    print(char)
    print("")
    if char.isdigit():
        #print(char)
        #print(type(char))
        char = int(char)
        #print(type(char))
        char += 1
        #print(char)
        
        rf.close()
        with open('data2.txt', 'w') as f:
            f.write(str(char))
        display_alt.setDisplay(char)
    else:
        print("ERROR: Day count is not an integer")

def logDate():
    global char

    DateNTime = datetime.now()
    startCount = (int(char) - 1)
    endCount = int(char)

    log = str("{}: Progressed {} days to {} days \n".format(DateNTime, startCount, endCount))
    
    with open('date_log.txt', 'a') as f:
        f.write(log)

def monday():
    global char

    rf = open('data2.txt', 'r') 
    rf.seek(0)
    char = str(rf.read(3))

    print(char)
    print("")
    if char.isdigit():
        #print(char)
        #print(type(char))
        char = int(char)
        #print(type(char))
        char += 3
        #print(char)
        
        rf.close()
        with open('data2.txt', 'w') as f:
            f.write(str(char))

    else:
        print("ERROR: Day count is not an integer")

    DateNTime = datetime.now()
    startCount = (int(char) - 3)
    endCount = int(char)

    log = str("{}: Counted Weeked; Progressed {} days to {} days \n".format(DateNTime, startCount, endCount))
    
    with open('date_log.txt', 'a') as f:
        f.write(log)


while True:
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    print(time , coolDown , char)
    if time == "12:32:40" and coolDown == False:

        wdDate = date.today()
        wdDay = calendar.day_name[wdDate.weekday()]

        if wdDay == "Monday" and countWeekends == True:
            monday()
            print("Mondays")
        else:
            counter()
            logDate()
            print("YO")

        coolDown = True
    elif time == "07:41:00" and coolDown == True:
        coolDown = False
    else:
        continue