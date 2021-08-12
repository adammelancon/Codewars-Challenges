def get_middle(s):
    if len(s) % 2 == 0:
        print("--------Even----------")
        print("is even")
        half = int(len(s) / 2)
        half += 1
        # print(half)
        halfminusone = int(int(half) - 2)
        # print(halfminusone)
        letters = [char for char in s]
        print(letters)
        print("".join(letters[int(halfminusone):int(half)]))
        return "".join(letters[int(halfminusone):int(half)])

        print("---------EVEN-end--------")
        print("")
    else:
        print("~~~~~~~ODD~~~~~~~~~")
        print("is odd")
        letters = [char for char in s]
        half = int(len(s) / 2)
        print(letters)
        print(half)
        print(letters[half])
        return letters[half]
        print("~~~~~~~ODD~end~~~~~~~~")
        print("")
        

get_middle("test")#,"es")
get_middle("testing")#,"t")
get_middle("middle")#,"dd")
get_middle("A")#,"A")
get_middle("of")#,"of")