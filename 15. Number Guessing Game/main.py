from art import logo
import random


def guess():
    print(logo)
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ")
    chances = 10 if difficulty == 'easy' else 5
    while chances > 0:
        choice = int(input("\nMake a guess : "))
        if choice == number:
            print(f"You got it. The number was {number}")
            print("Guess Again.")
            return
        elif choice > number:
            print("Too High")
        elif choice < number:
            print("Too Low")
        chances -= 1
        if chances == 0:
            print("You have run out of guesses. You lose.")
        else:
            print(
                f"You have {chances} attempts remaining to guess the number.")


guess()

if input("\nDo you want to play again? Type 'y' or 'n' : ") == 'y':
    guess()

print("GoodBye!")
