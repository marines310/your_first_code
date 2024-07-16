#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Hello, this is your tip calculator")
bill = float(input("How was the total bill? $"))
tip_question = float(input("How much tip would you like to pay? "))
people = int(input("How many people are going to split the bill? "))

tip_percent = tip_question / 100
tip_amount = tip_percent * bill
total_amount = bill + tip_amount
per_person = round(total_amount / people, 2)
per_person = "{:.2f}".format(total_amount / people)

print (f"The total amount each person sould pay is {per_person}")


# Below is an alternative version
# print("Hello, this is a tip calculator")
# total_price = float(input("What's the total bill?"))
# tip_amount = float(input("How much would you like to tip?"))
# num_people = int(input("How many people are there in total?"))

# print(f"Your total due is" + (total_price * ({tip_amount}+1) / num_people))

import # Module Testing
print (valueTest * 2)