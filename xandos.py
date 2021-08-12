# https://www.codewars.com/kata/55908aad6620c066bc00002a

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