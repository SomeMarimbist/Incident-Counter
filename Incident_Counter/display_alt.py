import board
import neopixel

ledHundreds = neopixel.NeoPixel(board.D18, 21, bpp=3)
ledTens = neopixel.NeoPixel(board.D20, 21, bpp=3)
ledOnes = neopixel.NeoPixel(board.D21, 21, bpp=3)
lines = []


def off():
    for i in range(3):
        if i == 0:
            for j in range(21):
                ledHundreds[j] = (0,0,0)
        if i == 1:
            for j in range(21):
                ledTens[j] = (0,0,0)
        if i == 2:
            for j in range(21):
                ledOnes[j] = (0,0,0)
        
        

def on(lightNum, digit):
    if digit == 0:
        ledHundreds[(lightNum*3) + i] = (255, 0, 0)
        print(lightNum)

    if digit == 1:
        ledTens[(lightNum*3) + i] = (255, 0, 0)
        print(lightNum)

    if digit == 2:
        ledOnes[(lightNum*3) + i] = (255, 0, 0)
        print(lightNum)
    


def setDisplay(number):
    split = [0, 0, 0]
    temp = [int(x) for x in str(number)]
    length = len(temp)
    for i in range(length):
        split[(3 - length + i)] = temp[i]
    off()
    for place in range(3):
        if split[place] == 0:
            on(0, place)
            on(1, place)
            on(2, place)
            on(3, place)
            on(4, place)
            on(5, place)
        if split[place] == 1:
            on(0, place)
            on(5, place)
        if split[place] == 2:
            on(4, place)
            on(5, place)
            on(6, place)
            on(2, place)
            on(1, place)
        if split[place] == 3:
            on(4, place)
            on(5, place)
            on(6, place)
            on(0, place)
            on(1, place)
        if split[place] == 4:
            on(3, place)
            on(6, place)
            on(5, place)
            on(0, place)
        if split[place] == 5:
            on(4, place)
            on(3, place)
            on(6, place)
            on(0, place)
            on(1, place)
        if split[place] == 6:
            on(4, place)
            on(3, place)
            on(2, place)
            on(1, place)
            on(0, place)
            on(6, place)
        if split[place] == 7:
            on(4, place)
            on(5, place)
            on(0, place)
        if split[place] == 8:
            on(0, place)
            on(1, place)
            on(2, place)
            on(3, place)
            on(4, place)
            on(5, place)
            on(6, place)
        if split[place] == 9:
            on(6, place)
            on(3, place)
            on(4, place)
            on(5, place)
            on(0, place)
            on(1, place)
        leds.show()

setDisplay(1)
