# https://www.codewars.com/kata/525f50e3b73515a6db000b83

'''
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
Example

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!

'''
def create_phone_number(n):
    
    ph1 = [str(x) for x in n[0:3]]
    ph1r = str("".join(ph1))
    print(ph1r)

    ph2 = [str(x) for x in n[3:6]]
    ph2r = str("".join(ph2))
    print(ph2r)
    
    ph3 = [str(x) for x in n[6:11]]
    ph3r = str("".join(ph3))
    print(ph3r)
    print("---------------------------------")
    print("(" + ph1r + ") " + ph2r + "-" + ph3r)
    return "(" + ph1r + ") " + ph2r + "-" + ph3r

    




create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
# create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
# create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0])
# create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])