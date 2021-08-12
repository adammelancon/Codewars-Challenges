import string

def is_pangram(s):
    lettercount = 0
    letters = [char for char in s]
    abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    lettersused = []
    for i in letters:
        if i not in lettersused:
            if i.lower() in abc:
                lettersused.append(i.lower()) 
                lettercount += 1
                # print(lettercount)
    print(lettersused)
    
    if lettercount >= 26:
        print("True")
        return True
    
    else:
        print("False")
        return False

pangram = "The quick, brown fox jumps over the lazy dog!"
is_pangram(pangram)    