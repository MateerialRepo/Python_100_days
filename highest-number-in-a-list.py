numbers = input("Type in the list of numbers ").split()
for n in range(0, len(numbers)):
    numbers[n] = int(numbers[n])
print(numbers)
highest_number = numbers[0]
for num in numbers:
    if highest_number < num:
        highest_number = num

print(f"The highest number in the list is {highest_number}")