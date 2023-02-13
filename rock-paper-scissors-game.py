import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_options = [rock, paper, scissors]
print("Welcome to the Rock, Paper, Scissors game \n")
while True:
    usr_Input = int(input("Please type 0 for Rock, 1 for Paper or 2 for Scissors: \n"))
    if usr_Input < 0 or usr_Input > 2:
        print("You have entered an invalid number")
        continue
    else:
        usr_opt = game_options[usr_Input]
        print(f"You chose:\n {usr_opt}")

    com_Input = random.randint(0, 2)
    com_opt = game_options[com_Input]

    print(f"Computer chose:\n {com_opt}")

    if usr_Input == 0 and com_Input == 2:
        print("You Win!!!")
        exit()
    elif com_Input == 0 and usr_Input == 2:
        print("You Lose")
        exit()
    elif usr_Input > com_Input:
        print("You win")
        exit()
    elif usr_Input < com_Input:
        print("You Lose")
        exit()
    else:
        print("It's a draw, Play again\n")
