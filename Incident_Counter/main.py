from os import startfile
from time import sleep

protein = "More"

startDelay = float(0.1)

print("Starting Files...")
#input("Starting Files: Press ENTER")
startfile("counter.py")
print("Launching counter.py")
sleep(startDelay)
startfile("terminal.py")
print("Launching terminal.py")
