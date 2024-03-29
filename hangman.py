# Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. For each letter
#  in the chosen_word, add a "_" to 'display'. So if the chosen_word was "apple", display should be ["_", "_", "_",
#  "_", "_"] with 5 "_" representing each letter to guess.
chosen_word = random.choice(word_list)
display = []
for letter in chosen_word:
    display.append("_")

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
guess = input("Guess a letter: ").lower()
guessed_letter_position = 0
for position in range(len(chosen_word)):
    if chosen_word[position] == guess:
        display[position] = guess

# TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter
#  replace with "_". Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)
