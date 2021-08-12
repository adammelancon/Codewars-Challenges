# https://www.codewars.com/kata/514b92a657cdc65150000006

def solution(number):
    anumber = []
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            anumber.append(i)
            print(i)
    print(sum(anumber))
solution(10)