# Random Winner Test

# OOP
# 1. Designate list
familymembers = ["Dad", "Mom", "Brandon", "Hailey", "Mike"]
# 2. Import Random
import random

# 3. Create random number format
numitems = len(familymembers)
numgen = random.randint(0, numitems -1)

# 4. Code for statement
print (f"{familymembers[numgen]} is the winner!")