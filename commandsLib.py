def countAdd():
    from datetime import datetime

    addDT = datetime.now()


    print("AAAAAAHHHHHH")
    rf = open('data2.txt', 'r') 
    rf.seek(0)
    char = rf.read(3)

    if char.isdigit():
        char = int(char)
        char += 1
        rf.close()
        with open('data2.txt', 'w') as f:
            f.write(str(char))
        with open('date_log.txt', 'a') as af:
            af.write("{}: Added 1, making {} \n".format(addDT, char))
            
    else:
        print("ERROR: Day count is not an integer")

    print("Added 1 day, it has now been {} day(s)".format(char))
    
def countAddMult():
    addCount = input("How mnay days will be added?: ")
    if addCount.isdigit():
        rf = open('data2.txt', 'r') 
        rf.seek(0)
        char = rf.read(3)
        if char.isdigit(): 
            char = int(char)
            char += int(addCount)
            rf.close()
            with open('data2.txt', 'w') as f:
                f.write(str(char))
        else:
            print("ERROR: Day count is not an integer")

        print("Added {} day(s), it has now been {} day(s)".format(addCount, char))
    else:
        print("ERROR: Argument is not an ingiger")

def countSub():
    rf = open('data2.txt', 'r') 
    rf.seek(0)
    char = rf.read(3)

    if char.isdigit():
        char = int(char)
        char -= 1
        rf.close()
        with open('data2.txt', 'w') as f:
            f.write(str(char))

    else:
        print("ERROR: Day count is not an integer")

    print("Removed 1 day, it has now been {} day(s)".format(char))

def countSubMult():
    print("AAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHH")
    addCount = input("How mnay days will be removed?: ")
    if addCount.isdigit():
        rf = open('data2.txt', 'r') 
        rf.seek(0)
        char = rf.read(3)
        if char.isdigit(): 
            char = int(char)
            char -= int(addCount)
            rf.close()
            with open('data2.txt', 'w') as f:
                f.write(str(char))
            print("Removed {} day(s), it has now been {} day(s)".format(addCount, char))
        else:
            print("ERROR: Day count is not an integer")
    else:
        print("ERROR Argument is not an intiger")
        
def reset():
    from datetime import datetime

    resetDT = datetime.now()

    with open('data2.txt', 'w') as wf:
            wf.write('0')
    with open('date_log.txt', 'a') as af:
            af.write("{}: Counter was reset to 0 \n".format(resetDT))
    print("set to 0")

def setCount():
    from datetime import datetime

    setDT = datetime.now()


    setTo = input("What will you set the days to?: ")
    if setTo.isdigit():
        with open('data2.txt', 'w') as f:
            f.write(setTo)
        with open('date_log.txt', 'a') as af:
            af.write("{}: Counter was set to {} \n".format(setDT, setTo))
        print("The day count has been set to " + setTo)
    else:
        print("ERROR Argument is not an intiger")

def kill():
    exit("counter.py")

def printDays():
    with open ('data2.txt', 'r') as f:
        dayCount = f.read(3)
    print("It has been {} days since the last incident".format(dayCount))

def comInfo():
    print("Commands List: ")
    print("/add           Adds 1 to the counter")
    print("/add+          Adds multiple to the counter")
    print("/sub           Removes 1 from the counter")
    print("/sub+          Removes multiple from the counter")
    print("/reset         Sets the counter to 0")
    print("/set           Sets the counter to a specified number")
    print("/kill          Stops all Incident Counter programs")
    print("/print         Gives the current amount of days counted")
    print("/info          Gives a list of valid commands in the ternminal")
    print("/date          Prints the date log into the terminal")
    print("/report        Prints the report log in JSON format")
    print("/report+       Prints a specific report in string format")
    print("/report++      Creates a report log")

def openDateLog():
    print("show date log")
    rf = open('date_log.txt', 'r')
    line = rf.readline()
    while line:
        print(line, end='')
        line = rf.readline()
    rf.close()

def openReportLog(): 
    import json 
    
    a = '{"name": "date", "incidentType": "otherInfo"}'
    
    y = json.loads(a) 
    
    print("JSON string = ", y) 
    print() 

    f = open ('incident_log.json', "r") 
    
    data = json.loads(f.read()) 
    
    for i in data['reports']: 
        print(i) 
    
    f.close() 

def invalid():
    print("ERROR: Invalid Command")

#Make non-int fail safe for numeric command arguments


#commands:
#Add 1 [Needs JSON]
#Add multiple [Needs JSON]
#Subtract 1 [Needs JSON]
#Subtract multiple [Needs JSON]
#Reset [Needs JSON]
#End Counter
#Print Current [Needs JSON]
#Command list
#view date log
#view incident report log
