# Create a hangman game

import random
import Hangman_words
import Hangman_art


print(Hangman_art.logo)
chosen_word = random.choice(Hangman_words.word_list)
word_length = len(chosen_word)
lives = 6
print(chosen_word)


display = list(word_length * "_")

end_of_game = False

while not end_of_game:
    guess = input("\nGuess a letter : ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
        print("---------------------------------------")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess

    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        lives -= 1
        print(
            f"\nYou guessed {guess}, that's not in the word. You lose a life.")
        print("---------------------------------------")
        print(Hangman_art.stages[lives])
        if lives == 0:
            end_of_game = True
            print("\nYou Lose".upper())

    if "_" not in display:
        end_of_game = True
        print("\nYou won".upper())
