# https://www.codewars.com/kata/57a0e5c372292dd76d000d7e
'''
Write a function called repeatStr which repeats the given string string exactly n times.
repeatStr(6, "I") // "IIIIII"
repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"
'''

def repeat_str(repeat, string):
        print(str(string) * int(repeat))


repeat_str(4, 'a')
repeat_str(3, 'hello ')
repeat_str(2, 'abc')