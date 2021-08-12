# https://www.codewars.com/kata/554b4ac871d6813a03000035

def high_and_low(numbers):
    li = list(numbers.split(" "))
    lint = list(map(int, li))
    print(str(max(lint)) + " " + str(min(lint)))
 
 
high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")#, "542 -214");
high_and_low("1 -1")#, "1 -1");
high_and_low("1 1")#, "1 1");
high_and_low("-1 -1")#, "-1 -1");
high_and_low("1 -1 0")#, "1 -1");
high_and_low("1 1 0")#, "1 0");        
high_and_low("-1 -1 0")#, "0 -1");
high_and_low("42")#, "42 42");