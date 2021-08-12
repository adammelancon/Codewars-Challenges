# https://www.codewars.com/kata/56f69d9f9400f508fb000ba7

def monkey_count(n):
    munkeys = []
    for x in range(n):
        munkeys.append(x + 1)
    print(munkeys)
    return munkeys

monkey_count(5)#, [1, 2, 3, 4, 5])
monkey_count(3)#, [1, 2, 3])
monkey_count(9)#, [1, 2, 3, 4, 5, 6, 7, 8, 9])
monkey_count(10)#, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
monkey_count(20)#, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])