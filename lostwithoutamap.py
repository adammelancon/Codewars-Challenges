# https://www.codewars.com/kata/57f781872e3d8ca2a000007e
# Given an array of integers, return a new array with each value doubled.

def maps(a):
    print(a)
    double  = []
    for i in a:
        double.append(i * 2)
    print(double)



maps([1, 2, 3])
maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
maps([])