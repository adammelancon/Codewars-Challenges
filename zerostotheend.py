# https://www.codewars.com/kata/52597aa56021e91c93000cb0
'''
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
'''

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