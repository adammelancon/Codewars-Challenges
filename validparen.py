# https://www.codewars.com/kata/52774a314c2333f0a7000688

# UNFINISHED

def valid_parentheses(string):
    newlist = [x for x in string] 
    print(str(newlist) + "   ===   " + string)
    only = [x for x in newlist if (x == "(") or (x == ")")]
    print("")
    print(str(only) + "   ===   " + string)
    print("===================================")

    for x in only:
        if x == ")":
            pass
            
 


 


    # if (")" not in string) and ("(" not in string):
        # print("No Parentheses:  " + string)
    # elif (")"  in string) and ("(" in string):
        # if [x for x in string == ")"]:
            # print("Wrong direction first:  " + string)
            # 
    # else:
        # print("Parentheses in correct direction:  " + string)


'''
Write a function that takes a string of parentheses, and determines if the order of the 
parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. 
Furthermore, the input string may be empty and/or not contain any parentheses at all. 
Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
'''


        









valid_parentheses("  (")#,False)
valid_parentheses(")test")#,False)
valid_parentheses("")#,True)
valid_parentheses("hi())(")#,False)
valid_parentheses("hi(hi)()")#,True)