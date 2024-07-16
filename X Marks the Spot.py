line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")
position = input("Where's the treasure?") # Where do you want to put the treasure?

letterformat = position[0].lower()
columnindex = ["a", "b", "c"]
inputletterindex = columnindex.index(letterformat)
print (inputletterindex)

