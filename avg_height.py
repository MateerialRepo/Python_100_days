heights = input("Type in the list of heights ").split()
for n in range(0, len(heights)):
    heights[n] = int(heights[n])
print(heights)
sum_of_heights = 0
for num in heights:
    sum_of_heights += num
average_height = sum_of_heights / len(heights)
print(f"The average height is {round(average_height)}")
