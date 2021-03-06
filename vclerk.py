# https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8
'''
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. 
Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.
Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.
Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?
Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.
'''

def tickets(people):
    customer = 0
    print("")
    print("")
    print("")
    print(people)
    twentyfives = 0
    fifties = 0
    hundreds = 0
    totalmoney = 0
    howmanyneed = 0 
    mnychg = 0 

    for i in people:
        if i == 25:           # check to see if they pay with a 25
            twentyfives += 1  # if it is a 25 add 1 to the 25's list
            totalmoney += i
        elif i == 50:
            fifties += 1
            totalmoney += i
        else:
            hundreds += 1
            totalmoney += i
        
        if i > 25:
            howmanyneed += ((i -25) / 25)
            twentyfives -= 1
            mnychg = totalmoney - i
        elif mnychg > i:
            return "YES"
            


        customer += 1
        # totalmoney = (twentyfives * 25) + (fifties * 50)  + (hundreds + 100)
        print("Customer: " + str(customer) + " hands me a " + str(i))
        print("Total money = " + str(totalmoney))
        print("how many 25's needed to hand back for change: " + str(howmanyneed))
        print("I now have " + str(twentyfives) + " 25")
        print("----------------------------")
    
    

    if howmanyneed >= 1:
        
        if twentyfives >= howmanyneed:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Yes, I can give " + str(howmanyneed) + " 25 bills")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("return YES")
            return str("YES")
        elif mnychg > i:
            pass
        else:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("No, I can't give exact change.")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("return NO")
            return str("NO")
    else:
        if howmanyneed == 0:
            print("No change needed")
            print("return YES")
            return str("YES")


print("================================================================================================")
# tickets([25, 25, 50])
# tickets([25, 100])
# tickets([25, 25, 25, 25, 25, 25, 25, 25, 25, 25])
tickets([25, 25, 50, 100])

