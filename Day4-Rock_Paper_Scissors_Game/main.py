
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

#Write your code below this line 👇

# Need to convert the indices to correspond to each
# 0 for rock, 1 for paper, 2 for scissors
import random
choices = [rock, paper, scissors]

user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
computer_choice = random.randint(0, 2)

# check to make sure the user input is valid. Not not proceed if the input isn't valid
if user_choice >= 3 or user_choice < 0:
    print("You type an invalid number, you lose")
# if user input is valid than proceed with the rest of the script
else:
    print(choices[user_choice])
    print('Computer chose:')
    print(choices[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose")
    elif user_choice > computer_choice:
        print("You Win")
    elif computer_choice > user_choice:
        print("You Lose")
    elif user_choice == computer_choice:
        print("It's a draw")
