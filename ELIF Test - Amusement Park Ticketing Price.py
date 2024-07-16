print ("Hello welcome to Fun Land")
print ("Before we let you in, we need to check if you meet the minimum age requirement")
height_challenge = int(input ("How tall are you?"))

if height_challenge > 100:
    print ("Welcome in! Your ticket is $10")
    age_challenge = int(input ("What's your age?"))
    if age_challenge > 15:
        print ("Your tiket is $20")
    elif age_challenge > 10:
        print ("Your ticket is $15")
    else:
        print ("Your ticket price is $10")
else:
    print ("Sorry but you're too short")