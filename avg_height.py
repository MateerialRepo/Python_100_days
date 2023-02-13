numbers = input("Type in the list of heights ").split()
for n in range(0, len(numbers)):
    numbers[n] = int(numbers[n])
print(numbers)
sum_of_numbers = 0
for num in numbers:
    sum_of_numbers += num
average_height = sum_of_numbers / len(numbers)
print(f"The average height is {round(average_height)}")
