# https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0
'''
It's pretty straightforward. Your goal is to create a function 
that removes the first and last characters of a string. You're given one parameter, 
the original string. You don't have to worry with strings with less than two characters.
'''
def remove_char(s):
    if len(s) >= 2:
        print(s[1:-1])



remove_char('eloquent')
remove_char('country')
remove_char('person') 
remove_char('place')
remove_char('ok')
remove_char('ooopsss')