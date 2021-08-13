# https://www.codewars.com/kata/59cf805aaeb28438fe00001c/train/python
# It involves implementing a program that sums the digits of a non-negative integer. For example, the sum of 3433 digits is 13.

def sum_of_digits(digits):
    if digits == None:
        print("")
        return None
    else:
        pass
    num_list = [int(i) for i in str(digits)]
    # print(f"num_list = {num_list}")

    answer = sum(num_list)
    # print(f"answer = {answer}")

    str_list = [str(i) for i in str(digits)]
    print(" + ".join(str_list) + " = " + str(answer))
    return " + ".join(str_list) + " = " + str(answer)
    
        

sum_of_digits("3433")#, "3 + 4 + 3 + 3 = 13")
sum_of_digits("64323")#, "6 + 4 + 3 + 2 + 3 = 18")
sum_of_digits("8")#, "8 = 8")

sum_of_digits(3433)#, "3 + 4 + 3 + 3 = 13")
sum_of_digits(64323)#, "6 + 4 + 3 + 2 + 3 = 18")
sum_of_digits(8)#, "8 = 8")

sum_of_digits(None)#, "")