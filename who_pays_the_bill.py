import random

# this s a program to choose who pays the bill from a list of random names

names = input("Please enter everybody's names separated by a comma ',': ")
name_list = names.split(",")
# random_int = random.randint(0, (len(name_list) - 1))
# who_pays = name_list[random_int]
who_pays = random.choice(name_list)

print(f"{who_pays} is going to pay for today's meal")
