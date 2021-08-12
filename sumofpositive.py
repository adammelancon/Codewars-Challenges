# https://www.codewars.com/kata/5715eaedb436cf5606000381

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