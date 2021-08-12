# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1

'''
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic 
characters and numeric digits that occur more than once in the input string. 
The input string can be assumed to contain only alphabets 
(both uppercase and lowercase) and numeric digits.
'''
def duplicate_count(text):
    debug = False
    text = text.lower()
    letters = ([char for char in text])
    
    if debug:
        print(letters)
        print(len(letters))


    dupe_count = {}
    for i in range(0, len(letters)):
        count = letters.count(letters[i])
        dupe_count[letters[i]] = count
        # if count not in dupe_count:
        #     dupe_count.append(int(count))
    
    if debug:
        print(dupe_count)  
    
    final_dupe_count = 0
    for number in dupe_count.values():
        if number > 1:
            final_dupe_count += 1

    print(f"FINAL ANSWER: {final_dupe_count}")
    return final_dupe_count
   
duplicate_count("")#, 0)
duplicate_count("abcde")#, 0)
duplicate_count("abcdeaa")#, 1)
duplicate_count("abcdeaB")#, 2)
duplicate_count("Indivisibilities")#, 2)