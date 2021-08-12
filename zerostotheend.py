def move_zeros(array):
    # print(array)
    count = 0
    for i in array:
        if i == 0:
            count += 1
    # print(count)   
    
    array = [x for x in array if x != 0]
    zerolist = [0] * count
    print(array)
    print(zerolist)
    print(array + zerolist)
    # digits = ', '.join(str(num) for num in array)
    # zeros = ', '.join(str(num) for num in zerolist)
    # finallist = array.extend(zerolist)
    # print(finallist)
    # print(digits + "," + str(zeros))
    # return digits + str(count)
    

move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])
# move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])