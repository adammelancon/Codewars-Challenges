# https://www.codewars.com/kata/54da5a58ea159efa38000836

def find_it(seq):
    oddnum = int()

    for i in seq:
        # print(str(i) + " occurs " + str(seq.count(i)) + " times.")
        if not seq.count(i) % 2 == 0:
            oddnum = i
            # print(str(i) + " occurs " + str(seq.count(i)) + " times.")

    print(oddnum)
    return oddnum







find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])#, 5)
find_it([1,1,2,-2,5,2,4,4,-1,-2,5])#, -1); 
find_it([20,1,1,2,2,3,3,5,5,4,20,4,5])#, 5);
find_it([10])#, 10);
find_it([1,1,1,1,1,1,10,1,1,1,1])#, 10);
find_it([5,4,3,2,1,5,4,3,2,10,10])#, 1);