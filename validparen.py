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


        









valid_parentheses("  (")#,False)
valid_parentheses(")test")#,False)
valid_parentheses("")#,True)
valid_parentheses("hi())(")#,False)
valid_parentheses("hi(hi)()")#,True)