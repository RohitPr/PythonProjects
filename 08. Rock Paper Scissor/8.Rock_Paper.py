# Rock Paper Scissors game

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

choice = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors : "))
print(game_images[choice])

options = ['rock', 'paper', 'scissors']
result = random.randint(0, 2)
print("Computer chose : ")
print(game_images[result])
print(options[result])

if choice == 0 and result == 2:
    print("\nYou Won")
elif choice == 0 and result == 1:
    print("\nYou Lose")
elif choice == 1 and result == 0:
    print("\nYou Won")
elif choice == 1 and result == 2:
    print("\nYou Lose")
elif choice == 2 and result == 1:
    print("\nYou Won")
elif choice == 2 and result == 0:
    print("\nYou Lose")
else:
    print("\nIt's a tie")
