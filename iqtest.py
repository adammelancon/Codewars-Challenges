def iq_test(numbers):
    nums = [int(x) for x in numbers.split(" ")]
    # print(nums)
    # print(type(nums))
    # print(type(nums[0]))
    odd = int()
    even = int()
    for i in nums:
        if i % 2 == 0:
            # print(str(i) + " is even")
            even += 1
        else:
            # print(str(i) + " is odd")
            odd += 1
    
    # print("Odds: " + str(odd) + " / " + "Evens: " + str(even))

    if odd == 1:
        # print("odd wins")
        for i in nums:
            if not i % 2 == 0:
                print(str(nums.index(i) + 1) + " < Solution")
                return str(nums.index(i) + 1)
                
    elif even == 1:
        # print("even wins")
        for i in nums:
            if  i % 2 == 0:
                print(str(nums.index(i) + 1) + " < Solution")
                return str(nums.index(i) + 1)





      

iq_test("2 4 7 8 10")#,3)
iq_test("1 2 2")#, 1)