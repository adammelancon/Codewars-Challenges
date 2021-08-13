# https://www.codewars.com/kata/5b6b128783d648c4c4000129
# Given a non-empty array of non-empty integer arrays, 
# multiply the contents of each nested array and return the smallest total.
import numpy

def smallest_product(a):
    small = []
    for i in a:
        small.append(numpy.prod(i))
    # print(min(small))
    return min(small)



smallest_product([[3, 2], [1, 2, 1], [7, 8]])#, 2)
smallest_product([[10], [3, 0], [-1, -6, 2]])#, 0)