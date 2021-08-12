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