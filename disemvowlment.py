# https://www.codewars.com/kata/52fba66badcd10859f00097e

def disemvowel(string_):
    vowels = ["a", "e", "i", "o", "u"]
    letters = [char for char in string_]
    output = []
    # lc = string_.lower()
    # print(lc)
    for i in letters:
        if i.lower() not in vowels:
            output.append(i)

    print("".join(output))
    



disemvowel("This website is for losers LOL!")