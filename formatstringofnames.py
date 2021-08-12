def namelist(names):
    nl = str()
    for i in range(len(names)):
        
        # print(str(i) + " --------------------Index Number")
        lastindex = len(names)
        # print(str(lastindex) + " -----------------Last Index Number")

        if int(len(names)) == 1:  # FOR ONLY ONE NAME IN LIST
            # print("  ---------------------------------------made it to one name only")
            for key in names[i]:
                x = names[i][key]
                nl = x #+ " -----------one name"

        elif int(len(names)) >= 2: # FOR MORE THAN ONE NAME IN LIST
            if i <= (lastindex - 3):
                for key in names[i]:
                  x = names[i][key]
                  nl = nl + x + ", "
                #   print(str(i) + "                 comma loop")
                #   print(nl)
            elif i == (lastindex - 2):
                for key in names[i]:
                  x = names[i][key]
                  nl = nl + x + " "
                #   print(str(i) + "                 space loop")
               
            elif i == (lastindex - 1):
                # print(str(i) +  "                  & loop")                   # FOR THE LAST ITEM IN THE LIST WITH &
                for key in names[i]:
                    x = names[i][key]
                    nl = nl + "& " + x  

    # print(str(len(names)) + " names.")
    print(nl)
    # print("==========================================================")    

    return nl

    
namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}])#, 'Bart, Lisa, Maggie, Homer & Marge',"Must work with many names")
namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}])#, 'Bart, Lisa & Maggie',"Must work with many names")
namelist([{'name': 'Bart'},{'name': 'Lisa'}])#, 'Bart & Lisa', "Must work with two names")
namelist([{'name': 'Bart'}])#, 'Bart', "Wrong output for a single name")
namelist([])#, '', "Must work with no names")