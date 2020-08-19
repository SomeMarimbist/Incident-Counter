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

def EndCommand():
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
                CountAdd()
                EndCommand()
            else:
                print("Invalid Password")
                EndCommand()
        
        elif userCom == "/add+":
            enteredPass = getpass("This command requires a password to execute: ")
            if enteredPass == password:
                CountAddMult()
                EndCommand()
            else:
                print("Invalid Password")
                EndCommand()
        
        elif userCom == "/sub":
            enteredPass = getpass("This command requires a password to execute: ")
            if enteredPass == password:
                CountSub()
                EndCommand()
            else:
                print("Invalid Password")
                EndCommand()
        
        elif userCom == "/sub+":
            enteredPass = getpass("This command requires a password to execute: ")
            if enteredPass == password:
                CountSubMult()
                EndCommand()
            else:
                print("Invalid Password")
                EndCommand()

        elif userCom == "/reset":
            enteredPass = getpass("This command requires a password to execute: ")
            if enteredPass == password:
                Reset()
                reportChoice = input("Do you want to file a report? (Y/N): ")
                if reportChoice.capitalize() == "Y":
                    WriteReport()
                elif reportChoice.capitalize() == "N":
                    print("A report will not be filed")
                else:
                    print("ERROR: Invalid response")
                    print("A report will not be filed")
                EndCommand()
            else:
                print("Invalid Password")
                EndCommand()

        elif userCom == "/set":
            enteredPass = getpass("This command requires a password to execute: ")
            if enteredPass == password:
                Set()
                EndCommand()
            else:
                print("Invalid Password")
                EndCommand()

        elif userCom == "/kill":
            enteredPass = getpass("This command requires a password to execute: ")
            if enteredPass == password:
                Kill()
                EndCommand()
            else:
                print("Invalid Password")
                EndCommand()
            
        elif userCom == "/print":
            PrintDays()
            EndCommand()

        elif userCom == "/info":
            ComInfo()
            EndCommand()

        elif userCom == "/date":
            OpenDateLog()
            EndCommand()

        elif userCom == "/report":
            OpenReportLog()
            EndCommand()

        elif userCom == "/report+":
            ReadReport()
            EndCommand()

        elif userCom == "/report++":
            enteredPass = getpass("This command requires a password to execute: ")
            if enteredPass == password:
                WriteReport()
                EndCommand()
            else:
                print("Invalid Password")
                EndCommand()
        else:
            Invalid()
            EndCommand()