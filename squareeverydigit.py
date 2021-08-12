# https://www.codewars.com/kata/546e2562b03326a88e000020
'''
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
Note: The function accepts an integer and returns an integer
'''

def square_digits(num):
    nums = []
    output = []
    for i in str(num):
        nums.append(i)
    # print(nums)
    for i in nums:
        output.append(int(i) ** 2)
    str_output = [str(output) for output in output]
    str_of_ints = "".join(str_output)
    print(str_of_ints)
    return int(str_of_ints)

square_digits(9119)#, 811181)
square_digits(0)# , 0)