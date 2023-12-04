MORSE_CODE = { 'A':'.-', 'B':'-...',      #[1-15]Define the translations of each letter
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

while True:
    print(" ")                                         #Break the line before each input
    message = input("input your message:").upper()     #Take user input and make it uppercase to make the Morse code dictionary work
    if message == ("Q-"):                              #[20-21]If the mesage is q- exit the code
        break
    for letter in message:                             #[22-23]Translate each letter of the message into Morse code and print the translated message with spaces between
        print(MORSE_CODE[letter], end=" ")
