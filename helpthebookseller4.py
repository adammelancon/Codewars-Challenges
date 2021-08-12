
# https://www.codewars.com/kata/54dc6f5a224c26032800005c

# UNFINISHED

def stock_list(listOfArt, listOfCat):
    if (len(listOfArt) == 0) or (len(listOfCat) == 0):
        return ""
    result = ""
    for cat in listOfCat:
        total = 0
        for book in listOfArt:
            if (book[0] == cat[0]):
                total += int(book.split(" ")[1])
        if (len(result) != 0):
            result += " - "
        result += "(" + str(cat) + " : " + str(total) + ")"
    print(result)
    
    




b = ['BOBB 100', 'CODA 100', 'BORT 100', 'BART 100', 'DRTY 100']
c = ['A', 'B', 'C', 'D']
stock_list(b,c)