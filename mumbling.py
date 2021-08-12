# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039

def accum(s):
    
    data = [char for char in s] #split text letters into a list
                                #data looks like this [Z,p,g,l,n,R,x,q,e,n,U]
    items = len(data)           #how many characters were submitted to the function at once
                                #items variable looks like this "11"
    fff = ''                    #blank variable to hold output
    index = -1                  #make a counter, but start at -1 so it skips 0 and 1 (1 is the uppercase letter) 
    for i in data:              #for each character in the list called data
        index += 1              #add one to the counter to keep track of the loop number
        output = []             #setup a list variable to hold the final output
        for x in range(1):                      #if this is the first round in the loop for the letter, make it an uppercase 
            output.append(i.capitalize())
        else:                                   #otherwise, make the letter a lowercase * the index number of the item in the list
            output = output + [i.lower()] * index
        
        if index < items - 1:                   #if this isn't the last item, add a "-" after it.
            output.append("-")
        else:
            output.append("")                   #at the end, don't put a - character
        fff = fff + "".join(output)             #join all the list items into a string with no spaces
    return fff                                  #return the result
        
out = accum("ZpglnRxqenU")
print(out)
