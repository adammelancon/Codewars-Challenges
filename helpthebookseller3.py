# https://www.codewars.com/kata/54dc6f5a224c26032800005c

# UNFINISHED

def stock_list(listOfArt, listOfCat):
    print("")
    print("---------------------------------------------------------------------------------------------------------------------")
    items = listOfArt # the items i have in stock
    print("Here are the 'ITEMS' I have along with inventory count:    " + str(items))
    needed = listOfCat # the categories i need total stock for
    # print("Here are the categories of inventory totals 'NEEDED':      " + str(needed))
    print("---------------------------------------")
    # output = []
                
    invnum = []
    for x in items:
        invnum.append([x.split(" ")[1]]) # get the inventory number

    category = [j[0] for j in items] # get categories I have in stock
    print("Here are the 'CATEGORY' I have in stock:                 " + str(category))
    print("here are the 'INVNUM' of items I have                    " + str(invnum))
    print("Here are categories I 'NEEDED' inventory totals for:     " + str(needed))
    print("---------------------------------------")
    print("")

    print("going into dict loop")

    itemdict = {}
    for i in category: # grabs B
        for x in invnum: # grabs 100
            itemdict[i] = itemdict[i] + x
            invnum.remove(x)
            break

    print(itemdict)

      
        # for i in needed : # for each category needed
        # print("-------------")
        # print("I have: " + str(category) + " categories")
        # print("I need: " + i)
        # for i in category:   
            # print(i)
            # output.append(i) 

    # if i in needed in category: 
    #    output.append(x)
    #    print("Appending " + str(x) + " to output list")
        #    print(str(x) + " - is NOT in the items I have in stock")
        #    needed.remove(x) # remove the category from the needed list
        #    print("Removed: " + str(x))
        #    print("Categories needed after removal: " + str(needed))


    # print(output)        
    # print("-------------")


b = ['BOBB 100', 'CODA 100', 'BORT 100', 'BART 100', 'DRTY 100']
c = ['A', 'B', 'C', 'D']
stock_list(b,c)

# b = ['BBAR 150', 'CDXE 515', 'BKWR 250', 'BTSQ 890', 'DRTY 600']
# c = ['A', 'B', 'C', 'D']
# stock_list(b, c)


# b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
# c = ["A", "B"]
# stock_list(b, c)
# output is "(A : 200) - (B : 1140)"