from time import sleep
from commandsLib import *
from getpass import getpass

import json
from jsonEditor import *


dateValid = True
augCache = 0
daysSince = 0
userCom = "null"
delay = float(0)
egg = True #egg cause why not?
logChoice = "null"
reportChoice = "null"
password = "egg"
enteredPass = "null"

def endCommand():
    global egg
    
    print("")
    sleep(delay)
    egg = False

while dateValid == True:
    userCom = "null"
    userCom = input("> ")
    egg = True

    while egg == True:        
        if userCom == "/add":
            enteredPass = getpass("This command requires a password to execute: ")
            if enteredPass == password:
                countAdd()
                endCommand()
            else:
                print("Invalid Password")
                endCommand()
        
        elif userCom == "/add+":
            enteredPass = getpass("This command requires a password to execute: ")
            if enteredPass == password:
                countAddMult()
                endCommand()
            else:
                print("Invalid Password")
                endCommand()
        
        elif userCom == "/sub":
            enteredPass = getpass("This command requires a password to execute: ")
            if enteredPass == password:
                countSub()
                endCommand()
            else:
                print("Invalid Password")
                endCommand()
        
        elif userCom == "/sub+":
            enteredPass = getpass("This command requires a password to execute: ")
            if enteredPass == password:
                countSubMult()
                endCommand()
            else:
                print("Invalid Password")
                endCommand()

        elif userCom == "/reset":
            enteredPass = getpass("This command requires a password to execute: ")
            if enteredPass == password:
                reset()
                reportChoice = input("Do you want to file a report? (Y/N): ")
                if reportChoice.capitalize() == "Y":
                    writeReport()
                elif reportChoice.capitalize() == "N":
                    print("A report will not be filed")
                else:
                    print("ERROR: Invalid response")
                    print("A report will not be filed")
                endCommand()
            else:
                print("Invalid Password")
                endCommand()

        elif userCom == "/set":
            enteredPass = getpass("This command requires a password to execute: ")
            if enteredPass == password:
                setCount()
                endCommand()
            else:
                print("Invalid Password")
                endCommand()

        elif userCom == "/kill":
            enteredPass = getpass("This command requires a password to execute: ")
            if enteredPass == password:
                kill()
                endCommand()
            else:
                print("Invalid Password")
                endCommand()
            
        elif userCom == "/print":
            printDays()
            endCommand()

        elif userCom == "/info":
            comInfo()
            endCommand()

        elif userCom == "/date":
            openDateLog()
            endCommand()

        elif userCom == "/report":
            openReportLog()
            endCommand()

        elif userCom == "/report+":
            readReport()
            endCommand()

        elif userCom == "/report++":
            enteredPass = getpass("This command requires a password to execute: ")
            if enteredPass == password:
                writeReport()
                endCommand()
            else:
                print("Invalid Password")
                endCommand()
        
        else:
            invalid()
            endCommand()