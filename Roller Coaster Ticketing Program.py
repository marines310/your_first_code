bill = 0

print ("Hello, welcome to the rollercoaster")

height = int(input("How tall are you?"))
if height >= 120:
    print ("Welcome")
    age = int(input ("What's your age?"))
    if age < 10:
        bill += 3
    elif age < 18:
        bill += 5
    else:
        bill += 8
    
    photo = input("Do you want a Photo? Y or N?")
    if photo == "Y":
        bill += 3
    
    print (f"Your total bill is ${bill}")
else:
    print ("Sorry, you're too short")