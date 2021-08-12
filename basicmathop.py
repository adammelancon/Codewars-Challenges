# https://www.codewars.com/kata/57356c55867b9b7a60000bd7

'''
Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.
'''
def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1 / value2




# tests
basic_op('+', 4, 7)
basic_op('-', 15, 18)
basic_op('*', 5, 5)
basic_op('/', 49, 7)