def CountAdd():
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
    else:
        print("ERROR: Day count is not an integer")

    print("Added 1 day, it has now been {} day(s)".format(char))
    
def CountAddMult():
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
        ("ERROR: Argument is not an ingiger")

def CountSub():
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

def CountSubMult():
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
        else:
            print("ERROR: Day count is not an integer")
        print("Removed {} day(s), it has now been {} day(s)".format(addCount, char))
    
    else:
        input()
        input("ERROR Argument is not an intiger")
        

def Reset():
    with open('data2.txt', 'w') as f:
            f.write('0')
    print("set to 0")

def Set():
    setTo = input("What will you set the days to?: ")
    with open('data2.txt', 'w') as f:
        f.write(setTo)
    print("The day count has been set to " + setTo)

def Kill():
    
    exit("counter.py")

def PrintDays():
    with open ('data2.txt', 'r') as f:
        dayCount = f.read(3)
    print("It has been {} days since the last incident".format(dayCount))

def ComInfo():
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

def OpenDateLog():
    print("show date log")
    rf = open('date_log.txt', 'r')
    line = rf.readline()
    while line:
        print(line, end='')
        line = rf.readline()
    rf.close()

def OpenReportLog(): 
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

def Invalid():
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
