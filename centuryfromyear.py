# https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097
'''
The first century spans from the year 1 up to and including the year 100, The second - from the year 101 up to and including the year 200, etc.
Task :

Given a year, return the century it is in.
'''
def century(year):
    if (year % 100) == 0:
        print(int(year/100))
    else:
        print(int(year / 100 -1))





century(1705)
century(1900)
century(1601)
century(2000)
century(356)
century(89)