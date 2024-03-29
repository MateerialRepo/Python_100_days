import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Hard Level - Order of characters randomised:
password = []
if nr_letters < 0:
    print("You have entered a number lower than zero.\n We would assume a value of 5 for the number of letters in your password")
    nr_letters = 5

if nr_numbers < 0:
    print("You have entered a number lower than zero.\n We would assume a value of 5 for the numbers in your password")
    nr_numbers = 5

if nr_symbols < 0:
    print("You have entered a number lower than zero.\n We would assume a value of 5 for the number of letters")
    nr_symbols = 5

for i in range(0, nr_symbols):
    symbol = random.choice(symbols)
    password.append(symbol)

for j in range(0, nr_numbers):
    number = random.choice(numbers)
    password.append(number)

# remaining_letters = nr_letters - (nr_symbols + nr_numbers)
for k in range(0, nr_letters):
    letter = random.choice(letters)
    password.append(letter)

random.shuffle(password)

generated_password = "".join(password)

print(f"Here is your password: {generated_password}")
