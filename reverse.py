# https://www.codewars.com/kata/5583090cbe83f4fd8c000051
'''
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
Example:
348597 => [7,9,5,8,4,3]
'''

def digitize(n):
    return [int(d) for d in reversed(str(n))]
    #return [char for char in reversed.n()]



digitize(35231)
digitize(23582357)
digitize(984764738)
digitize(45762893920),
digitize(548702838394)
