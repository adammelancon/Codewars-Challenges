def solution(s):
    letlist = []
    output = []
    letlist[:] = s
    joinout = []
    countstart = 0
    countend = 2

    if len(s) %2 == 0:
        evencount = 0
        for i in letlist:
            # print("i = " + str(i))
            # print(letlist[countstart:countend])
            if evencount % 2 == 0:
                joinout = "".join(letlist[countstart:countend])
                countstart = countstart + 2
                countend = countend + 2
                output.append(joinout)
                # print(joinout)
            evencount += 1
            # print("output = " + str(output))
    else:
        evencount = 0
        for i in letlist:
            if evencount % 2 == 0:
                joinout = "".join(letlist[countstart:countend])
                countstart = countstart + 2
                countend = countend + 2
                output.append(joinout)
            evencount += 1
        output = output[:-1]
        output.append(letlist[-1] + "_")
    return output
    print("output = " + str(output))

print("")
print("")
print("========================================")

solution("asdfadsf")#, ['as', 'df', 'ad', 'sf']),
solution("asdfads")#, ['as', 'df', 'ad', 's_']),
solution("")#, []),
solution("x")#, ["x_"]),
print("========================================")
print("")
print("")
