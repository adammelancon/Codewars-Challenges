# https://www.codewars.com/kata/57356c55867b9b7a60000bd7

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