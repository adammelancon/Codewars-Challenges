# https://www.codewars.com/kata/55908aad6620c066bc00002a
'''
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
Examples input/output:
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
'''

def xo(s):
    xcount = int()
    ocount = int()
    for i in s:
        if i.lower() == "x":
            xcount += 1
        elif i.lower() == "o":
            ocount += 1
        else:
            pass
    print("X's = " + str(xcount))
    print("O's = " + str(ocount))
    if xcount == 0:
        print("True")
        return True
    elif xcount == ocount:
        print("True")
        return True
    else:
        print("False")
        return False












xo('xo')#, 'True expected')
xo('xo0')#, 'True expected')
not xo('xxxoo')#, 'False expected')