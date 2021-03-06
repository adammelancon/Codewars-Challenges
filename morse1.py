# https://www.codewars.com/kata/54b724efac3d5402db00065e
# In this kata you have to write a simple Morse code decoder. 

MORSE_CODER = { 'A':'.-', 'B':'-...',
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
                    '(':'-.--.', ')':'-.--.-'}

MORSE_CODE = {'..-.': 'F', '-..-': 'X',
                 '.--.': 'P', '-': 'T', '..---': '2',
                 '....-': '4', '-----': '0', '--...': '7',
                 '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J',
                 '---': 'O', '-.-': 'K', '----.': '9', '..': 'I',
                 '.-..': 'L', '.....': '5', '...--': '3', '-.--': 'Y',
                 '-....': '6', '.--': 'W', '....': 'H', '-.': 'N', '.-.': 'R',
                 '-...': 'B', '---..': '8', '--..': 'Z', '-..': 'D', '--.-': 'Q',
                 '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A', '...': 'S', '.----': '1'}


def decodeMorse(morse_code):
    item = [x for x in morse_code.split(" ")]
    code = [x.strip() for x in item]
    # code = [x for x in code if  x]
    print("---------")
    print(code)
    print("---------")
    output = []
    for i in code:
        if len(i) >= 1:
            output.append(MORSE_CODE[i])
            print(MORSE_CODE[i])
        else:
            output.append(" ")
            print(" ")
    finalout = "".join(output)
    finalout = finalout.replace("  ", " ")
    print(finalout)
    return "".join(finalout)
decodeMorse('.... . -.--   .--- ..- -.. .')#, 'HEY JUDE')