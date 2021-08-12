# https://www.codewars.com/kata/546f922b54af40e1e90001da

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