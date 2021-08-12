# https://www.codewars.com/kata/515e271a311df0350d00000f

def square_sum(numbers):
    sqnm = [numbers ** 2 for numbers in numbers]
    return sum(sqnm)
    
square_sum([1,2])