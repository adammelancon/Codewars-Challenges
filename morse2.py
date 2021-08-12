MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G',
 '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
  '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U',
   '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1',
    '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
     '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'",
      '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':',
       '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"',
        '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}

#   morseCodes(".--") //to access the morse translation of ".--"

def decode_bits(bits):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    answer = bits.replace('111', '-').replace('000', ' ').replace('11', '.').replace('00', '')
    print(answer)
    return answer

def decode_morse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    answer = morseCode.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')
    print(answer)
    return answer

decode_morse(decode_bits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'))


# test.describe("Example from description")
# test_and_print(decode_morse(decode_bits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')), 'HEY JUDE')

# test.describe("Your own tests")
# Add more tests here