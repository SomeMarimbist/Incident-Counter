#import some gpio stuff here
from digitalio import DigitalInOut
import board

top = [DigitalInOut(board.D4), DigitalInOut(board.D17), DigitalInOut(board.D27)]
topLeft = [DigitalInOut(board.D22), DigitalInOut(board.D18), DigitalInOut(board.D24)]
topRight = [DigitalInOut(board.D25), DigitalInOut(board.D5), DigitalInOut(board.D6)]
middle = [DigitalInOut(board.D13), DigitalInOut(board.D19), DigitalInOut(board.D26)]
bottom = [DigitalInOut(board.D12), DigitalInOut(board.D16), DigitalInOut(board.D20)]
bottomLeft = [DigitalInOut(board.D2), DigitalInOut(board.D3), DigitalInOut(board.D14)]
bottomRight = [DigitalInOut(board.D10), DigitalInOut(board.D9), DigitalInOut(board.D11)]

def setDisplay(number):
    split = [int(x) for x in str(number)]
    reset()
    for place in range(3):
        if split[place] == 0:
            top[place] = True
            topLeft[place] = True
            topRight[place] = True
            bottom[place] = True
            bottomLeft[place] = True
            bottomRight[place] = True
        if split[place] == 1:
            topRight[place] = True
            bottomRight[place] = True
        if split[place] == 2:
            top[place] = True
            topRight[place] = True
            middle[place] = True
            bottom[place] = True
            bottomLeft[place] = True
        if split[place] == 3:
            top[place] = True
            topRight[place] = True
            middle[place] = True
            bottom[place] = True
            bottomRight[place] = True
        if split[place] == 4:
            topLeft[place] = True
            topRight[place] = True
            middle[place] = True
            bottomRight[place] = True
        if split[place] == 5:
            top[place] = True
            topLeft[place] = True
            middle[place] = True
            bottom[place] = True
            bottomRight[place] = True
        if split[place] == 6:
            top[place] = True
            topLeft[place] = True
            middle[place] = True
            bottom[place] = True
            bottomLeft[place] = True
            bottomRight[place] = True
        if split[place] == 7:
            top[place] = True
            topRight[place] = True
            bottomRight[place] = True
        if split[place] == 8:
            top[place] = True
            topLeft[place] = True
            topRight[place] = True
            middle[place] = True
            bottom[place] = True
            bottomLeft[place] = True
            bottomRight[place] = True
        if split[place] == 9:
            top[place] = True
            topLeft[place] = True
            topRight[place] = True
            middle[place] = True
            bottom[place] = True
            bottomLeft[place] = True

def reset():
    for place in range(3)
        top[place] = False
        topLeft[place] = False
        topRight[place] = False
        middle[place] = False
        bottom[place] = False
        bottomLeft[place] = False
        bottomRight[place] = False
