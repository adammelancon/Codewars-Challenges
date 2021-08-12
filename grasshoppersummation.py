# https://www.codewars.com/kata/55d24f55d7dd296eb9000030
# Write a program that finds the summation of every number from 1 to num. 
# The number will always be a positive integer greater than 0.

def summation(num):
    count = 0
    numbs = []
    while count < num:
        count += 1
        numbs.append(count)
    print(numbs)
    print("-----------------------------------------")
    print(sum(numbs))
    
    
    
    





summation(1) 
summation(8) 
summation(22)
summation(100)
summation(213)