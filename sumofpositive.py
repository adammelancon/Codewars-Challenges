# https://www.codewars.com/kata/5715eaedb436cf5606000381
'''
You get an array of numbers, return the sum of all of the positives ones.
Example [1,-4,7,12] => 1 + 7 + 12 = 20
Note: if there is nothing to sum, the sum is default to 0.
'''

def positive_sum(arr):
    posnum = []
    for i in arr:
        if i >= 0:
            posnum.append(i)
    done = sum(posnum)
    if done >=1:
         return done
    else:
        return 0


print(positive_sum([1,2,3,4,5]))

print(positive_sum([1,-2,3,4,5]))

print(positive_sum([-1,2,3,4,-5]))