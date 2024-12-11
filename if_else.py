print("welcome to the rollercoaster")
height = int(input("what is your height in cm?"))

if height >= 120:
     print("you can write the rollercoaster")
     age = int(input("what is your age?"))
     if age <= 12:
          print("pay $5")
     elif age <= 18:
          print("pay 7")
     else:
          print("5")
else:
     print("Sorry you have to grow more first")