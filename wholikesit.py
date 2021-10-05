'''
https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python
You probably know the "like" system from Facebook and other pages. 
People can "like" blog posts, pictures or other items. 
We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people 
that like an item. It must return the display text as shown in the examples:
'''

def likes(names):
    if len(names) == 0:
        return f"no one likes this"
    else:
        if len(names) == 1:
            return (f"{names[0]} likes this")
        if len(names) == 2:
            return (f"{names[0]} and {names[1]} like this")
        if len(names) == 3:
            return (f"{names[0]}, {names[1]} and {names[2]} like this")
        if len(names) >= 4:
            return (f"{names[0]}, {names[1]} and {int(len(names)) - 2} others like this")
    


likes([]) #, 'no one likes this')
likes(['Peter']) #, 'Peter likes this')
likes(['Jacob', 'Alex']) #, 'Jacob and Alex like this')
likes(['Max', 'John', 'Mark']) #, 'Max, John and Mark like this')
likes(['Alex', 'Jacob', 'Mark', 'Max']) #, 'Alex, Jacob and 2 others like this')
