# https://www.codewars.com/kata/55685cd7ad70877c23000102

def make_negative( number ):
    if number > 0:
        number = (number - number * 2)
        print(number)

make_negative(42)