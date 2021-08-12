# https://www.codewars.com/kata/563e320cee5dddcf77000158
# Return the average of the given array rounded down to its nearest integer.
# The array will never be empty.

def get_average(marks):
    #raise NotImplementedError("TODO: get_average")
    finalgrade = sum(marks) / len(marks)
    print(int(finalgrade))
    
    
    
    




get_average([2, 2, 2, 2]) #, 2, "didn't work for [2, 2, 2, 2]")
get_average([1, 5, 87, 45, 8, 8]) #, 25, "didn't work for [1, 5, 87, 45, 8, 8]")
get_average([2,5,13,20,16,16,10]) #, 11, "didn't work for [2,5,13,20,16,16,10]")
get_average([1,2,15,15,17,11,12,17,17,14,13,15,6,11,8,7]) #, 11, "didn't work for [1,2,15,15,17,11,12