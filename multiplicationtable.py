# https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/train/python
'''
Your task, is to create NxN multiplication table, of size provided in parameter.
for example, when given size is 3:
1 2 3
2 4 6
3 6 9
for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]
'''
def multiplication_table(size):
    size = int(size)
    table = []
    for i in range(size):
        nestlist = []
        for x in range(size):
            x = x + 1
            nestlist.append(x) # [1] [1, 2] [1, 2, 3]
        table.append(nestlist) # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    # print(table) # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    
    for i in range(size):   # i is nested list index number
        for x in range(size): # x will be the index of the nested list items
            y = (x + 1) * (i + 1)
            # print("==")
            # print(f"y is {y}")
            # print(f"i is {i}")
            # print(f"x is {x}")
            # print("~~")
            table[i][x] = y

    print(table)
    return table

multiplication_table(3)

        # create outside list
        # create number of nested lists based on size variable
        # for each nested list, do, nested list 0 = 1 * each item, nested list 1 = 2 * each item, 
        # nested list 2 = 3 * each item         etc... up to the size variable number
        # make each row * 1, then * 2, then * 3 for however many is in the size variable

    

