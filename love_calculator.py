# get both names.
# find the number of times the letters in true appear in both names
# find the number of times the letters in love appear in both names
# if love score is <10 or 90> the message is you go like coke and gala
# if the score is between 40 and 50 message is you are alright together
# else just give them the score

print("Welcome to Mateerial's love machine")
print("We help you determine your match with someone else")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

both_names = name1 + name2
# lowercase for both names
both_names_lower = both_names.lower()
# to check the count of "true" in the name
first_num = 0
second_num = 0
for w in "true":
    first_num += both_names_lower.count(w)
for x in "love":
    second_num += both_names_lower.count(x)

score_string = str(first_num) + str(second_num)
score = int(score_string)

if (score < 10) or (score > 90):
    print("Your score is ", score, ". You match like coke and gala")
elif 40 <= score <= 50:
    print(f"Your score is {score}, You are alright together")
else:
    print("Your score is ", score)
