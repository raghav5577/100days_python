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

game_images = [rock, paper, scissors]

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# Note: it's worth checking if the user has made a valid choice before the next line of code.
# If the user typed somthing other than 0, 1 or 2 the next line will give you an error.
# You could for example write:
# if user_choice < 0 or user_choice > 2:
print(game_images[user])

computer = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer])

if user >= 3 or user < 0:
    print("You typed an invalid number. You lose!")
elif user == 0 and computer == 2:
    print("You win!")
elif computer == 0 and user == 2:
    print("You lose!")
elif computer > user:
    print("You lose!")
elif user > computer:
    print("You win!")
elif computer == user:
    print("It's a draw!")
