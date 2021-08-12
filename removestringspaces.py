# https://www.codewars.com/kata/57eae20f5500ad98e50002c5

def no_space(x):
    letters = [char for char in x]
    output = []
    for i in letters:
        if i != " ":
            output.append(i)

    print("".join(output))        




no_space('8 j 8   mBliB8g  imjB8B8  jl  B')
no_space('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd')
no_space('8aaaaa dddd r     ')
no_space('jfBm  gk lf8hg  88lbe8 ')
no_space('8j aam')