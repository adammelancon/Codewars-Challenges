def data_reverse(data):
    n = 8
    output=[data[i:i + n] for i in range(0, len(data), n)]
    rev_lst = output[::-1]
    print(data)
    print(rev_lst)
    join_list = [x for sublist in rev_lst for x in sublist]
    print(join_list)
    return join_list


data1 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
data2 = [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
data_reverse(data1)

data3 = [0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1]
data4 = [0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0]
# data_reverse(data3)#,data4)