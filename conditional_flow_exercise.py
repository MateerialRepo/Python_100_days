print("Welcome to the rollercoaster!")
total_cost = 0
height = int(input("What is your height in cm? "))
if height > 120:
  print("You can ride the rollercoaster")
  age = int(input("Please enter your current age? "))
  if age<12:
    print("Please pay $5 for your ticket")
    total_cost = 5
  elif age <= 18:
    print("Please pay $7 for your ticket")
    total_cost = 7
  else:
    print("Please pay $12 for your ticket")
    total_cost = 12

  photos = input("do you want photos? yes or no? ")

  if photos.lower() == "yes":
    total_cost = total_cost+3
  else:
    total_cost
  
else:
  print("Sorry, but you have to grow taller to be able to ride the rollercoaster")

print(f"Your total fees is ${total_cost}")
