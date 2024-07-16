# List Practice

# Lists are a linear, sequential list of items
# Lists are created with square brackets "[" and "]" and you can include strings, integers, booleans and etc separated by commas in between
familymembers = ["Dad", "Mom", "Hailey", "Brandon", "Mike"]

# You can print individual items within lists by calling up a data point within a list through square brackets "[" and "]" and calling up a number in between
print (familymembers[2])

# You can edit data pieces within a list by calling up a datapoint and adding a new value to it:
familymembers[2] = "Seung Hyun"
print (familymembers)

# You can add a single datapoint to a list through an "append" command .append
familymembers.append("NEO")
print (familymembers)


# You can add to a list, another list through the "extend" command, .extend
# Because this is a function that's adding a list, YOU MUST INCLUDE FOR BOTH THE STANDARD BRACKETS AND SQUARE BRACKETS
familymembers.extend(["EXT1", "EXT2", "EXT3"])
print (familymembers)