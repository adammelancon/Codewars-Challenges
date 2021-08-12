# https://www.codewars.com/kata/54edbc7200b811e956000556

'''
Consider an array/list of sheep where some sheep may be missing from their place. 
We need a function that counts the number of sheep present in the array (true means present).
'''

def count_sheeps(sheep):
    tsheep = 0
    fsheep = 0
    #print(sheep)
    for i in sheep:
        #print(i)
        if i == True:
            tsheep += 1
            #print("True Sheep= " + str(tsheep))
        elif i == False:
            fsheep += 1
            #print("False Sheep= " + str(fsheep))
    print(tsheep)



array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ];

count_sheeps(array1)