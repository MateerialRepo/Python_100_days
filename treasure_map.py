# 🚨 Don't change the code below 👇
import math

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
# position = int(input("Where do you want to put the treasure? please write the column number followed by thw row number: "))
position = input("Where do you want to put the treasure? please write the column number followed by thw row number: ")

# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# column = (math.floor(position/10)) - 1
# row = (position % 10) - 1
column = int(position[0]) - 1
row = int(position[1]) - 1
map[row][column] = 'X'




#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")