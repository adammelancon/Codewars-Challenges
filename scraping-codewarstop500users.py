# https://www.codewars.com/kata/581c06b95cfa838603000435/train/python
'''
You should get and parse the html of the codewars leaderboard page.
https://www.codewars.com/users/leaderboard
Return a 'Leaderboard' object with a position property.
Leaderboard#position should contain 500 'User' objects.
Leaderboard#position[i] should return the ith ranked User(1 based index).

Each User should have the following properties
User#name    # => the user's username, not their real name
User#clan    # => the user's clan, empty string if empty clan field
User#honor   # => the user's honor points as an integer

Ex:
  an_alien = leaderboard.position[3]   # => #<User:0x3124da0 @name="myjinxin2015", @clan="China Changyuan", @honor=21446>
  an_alien.name                        # => "myjinxin2015"
  an_alien.clan                        # => "China Changyuan"
  an_alien.honor                       # => 21446
'''

from bs4 import BeautifulSoup
import requests

URL = 'https://www.codewars.com/users/leaderboard'

def solution():
  # do it
  return