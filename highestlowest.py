# https://www.codewars.com/kata/554b4ac871d6813a03000035
# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

def high_and_low(numbers):
    numlist = list(numbers.split())
    print(numlist)
    
    high = int()
    low = int()

    for i in numlist:
        
        i = int(i)
        # print(type(i))
        # print("i = " + str(i))

        if i >= high:
            print("i high: " + str(i))
            high = int(i)
            print("High: " + str(high))
            print("========")
        elif i <= high and i <= low:
            print("i low: " + str(i))
            low = int(i)
            print("Low: " + str(low))
            print("========")

    print("====------------------------====")    
        
        
    # print("numlist items= " + str(len(numlist)))
    if len(numlist) == 1:
        print(str(high))
    else:
        print(str(high) + " < HIGH - LOW > " + str(low))
    print("====------------------------====")


high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")#, "542 -214");
high_and_low("1 -1")#, "1 -1");
high_and_low("1 1")#, "1 1");
high_and_low("-1 -1")#, "-1 -1");
high_and_low("1 -1 0")#, "1 -1");
high_and_low("1 1 0")#, "1 0");        
high_and_low("-1 -1 0")#, "0 -1");
high_and_low("42")#, "42 42");