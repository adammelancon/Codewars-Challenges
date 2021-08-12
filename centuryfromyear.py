# https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097

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