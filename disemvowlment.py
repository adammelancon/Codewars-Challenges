# https://www.codewars.com/kata/52fba66badcd10859f00097e

'''
Trolls are attacking your comment section!
A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
Your task is to write a function that takes a string and return a new string with all vowels removed.
For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
Note: for this kata y isn't considered a vowel.
'''
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