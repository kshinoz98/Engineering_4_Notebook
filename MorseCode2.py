#type:ignore
import digitalio    #[2-4]Import necessary libraries
import board
import time

MORSE_CODE = { 'A':'.-', 'B':'-...',        #[6-20]Define the morse code alphabet
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-',' ':'/'}

led = digitalio.DigitalInOut(board.GP0)      #[22-23] Set up LED
led.direction = digitalio.Direction.OUTPUT

modifier = 0.25                              #[25-30] Set up timing
dot_time = 1*modifier
dash_time = 3*modifier
between_taps = 1*modifier
between_letters = 3*modifier
between_words = 7*modifier

while True:                                 #[32-38] For each letter of the message, translate into morse code and print
    print(" ")
    message = input("input your message:").upper()
    if message == ("Q-"):
        break
    for letter in message:
        print(MORSE_CODE[letter], end = " ")
    for letter in message:                   #[39-52] For each letter of the morse code message, blink the light for the alloted time or pause between letters or words
        morse_message = MORSE_CODE[letter]
        for x in morse_message:
            time.sleep(between_letters)
            if x == ".":
                led.value = True
                time.sleep(dot_time)
                led.value = False
            elif x == "-":
                led.value = True
                time.sleep(dash_time)
                led.value = False
            elif x == "/":
                time.sleep(between_words-between_letters)