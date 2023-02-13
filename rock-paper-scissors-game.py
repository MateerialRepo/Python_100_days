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

print("Welcome to the Rock, Paper, Scissors game \n")
while True:
    usr_Input = int(input("Please type 0 for Rock, 1 for Paper or 2 for Scissors: "))
    if usr_Input < 0 or usr_Input > 2:
        print("You have entered an incorrect option")
        exit()
    com_Input = random.randint(0, 2)
    options = [rock, paper, scissors]
    usr_opt = options[usr_Input]
    com_opt = options[com_Input]

    print(f"You chose:\n {usr_opt}")
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
