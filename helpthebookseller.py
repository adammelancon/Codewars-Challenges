# https://www.codewars.com/kata/54dc6f5a224c26032800005c

# UNFINISHED

def stock_list(listOfArt, listOfCat):
    print("")
    print("")
    report = {}
    category = ""
    inventory = ""
    
     
    for x in listOfArt:
        category = x[0]  # get first letter of category
        inventory = int(x.split(" ")[1]) # split inventory number from category

        # print(category)
        if category not in report:
            if category in listOfCat:
                report[category] = inventory
        else:
            report[category] += inventory       

    # print(listOfCat)
    output = ""
    print("Asking Category List: " + str(listOfCat))
    print(str(len(listOfCat)) + " categories in list now")
    print("categories in report summed up: " + str(report))
    for i in listOfCat:
        if i not in report:
            listOfCat.remove(i)
            print("Removed: " + i)
    
    print("list after removing not in there = " + str(listOfCat))
    print(str(len(listOfCat)) + " items in category list now") 
    print(str(listOfCat) + " categories in list")
    for x in sorted(listOfCat):
        print("")
        output =  str(output) + "(" + str(x) + " : " + str(report[x]) + ") "
        print("                      output after adding 1 item onto output variable: " + output)
        listOfCat.remove(x)
        print("Removing category " + x)
        print(str(len(listOfCat)) + " items in cat now")
        print(str(listOfCat) + " cat items remaining")
        
    
    print("FINAL OUTPUT: " + output)
    print("")
    print("")
    print(output)
    print(report)


    
    # def dashes(x):
        # d = ")"
        # s =  [e+d for e in x.split(d) if e]
        # print(s)
        #     

    # dashes(output)
    # return output
    #NEED TO GET DASHES WORKING ON NEXT TRY!!!
        


b = ['BBAR 150', 'CDXE 515', 'BKWR 250', 'BTSQ 890', 'DRTY 600']
c = ['A', 'B', 'C', 'D']
stock_list(b, c)







b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]
# 
# result should be (A : 200) - (B : 1140)
stock_list(b, c)