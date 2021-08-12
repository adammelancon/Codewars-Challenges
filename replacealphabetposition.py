# https://www.codewars.com/kata/546f922b54af40e1e90001da

'''
In this kata you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
"a" = 1, "b" = 2, etc.
Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)
'''

def alphabet_position(text):
    
    abc = [char for char in "abcdefghijklmnopqrstuvwxyz"]
    # print(abc)
    
    output = []
    for i in text:
        if i.lower() in abc:
            low = i.lower()
            letterindex = abc.index(low) + 1
            output.append(letterindex)
    # print(output)
    print(text)
    print(" ".join(str(v) for v in output))
    return " ".join(str(v) for v in output)

alphabet_position("The sunset sets at twelve o' clock.")
# alphabet_position("The narwhal bacons at midnight.")