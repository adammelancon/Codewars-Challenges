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