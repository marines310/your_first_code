year = 1700


if year % 4 == 0:
  if year % 100 != 0:
    print ("Leap year")
  elif year % 400 == 0:
    print ("Leap year")
  else:
    print ("Not leap year")
else:
  print ("Not leap year")