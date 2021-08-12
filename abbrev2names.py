# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3
'''Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

Patrick Feeney => P.F
'''

def abbrev_name(name):
    name = name.split(" ")
    first = [char for char in name[0]]
    first = str(first[0]) + ". "
    last = [char for char in name[1]]
    last = str(last[0]) + "."
    print(first + last)
    return first + last


abbrev_name("Sam Harris")
abbrev_name("Patrick Feenan")
abbrev_name("Evan Cole")
abbrev_name("P Favuzzi")
abbrev_name("David Mendieta")