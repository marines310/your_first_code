# Ticket Program
bill = 0
print ("Welcome")

# Basic Requirements Challenge
heightchallenge = int(input("Please type in your height "))
if heightchallenge >= 120:
    print ("You are tall enough to access")
    agechallenge = int(input("How old are you?"))
    if agechallenge > 21:
        bill += 20
    elif agechallenge < 21 and agechallenge > 2:
        bill += 10
    else:
        print ("You are not old enough to ride the rollercoaster")
else:
    print ("You are not tall enough to ride the rollercoaster")

# Photo Challenge
photochallenge = input("Would you like to order a photo? ").lower()
if photochallenge == "yes":
    bill += 5
else:
    bill += 0

# Final Summary
print (f"Your total bill for today is {bill}")