def is_square(n):

    def truesq(x):
        num = x ** 0.5
        modul = num % 1
        issqr = modul == 0
        return issqr

    if n < 0:
        print("False")
        return False
    elif truesq(n) == True:
        print("True")
        return True    
    else:
        print("False")
        return False
    
    







is_square(-1)#, False, "-1: Negative numbers cannot be square numbers")
is_square( 0)#, True, "0 is a square number (0 * 0)")
is_square( 3)#, False, "3 is not a square number")
is_square( 4)#, True, "4 is a square number (2 * 2)")
is_square(25)#, True, "25 is a square number (5 * 5)")
is_square(26)#, False, "26 is not a square number")