import random

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo, stages
print(logo)

# Create an empty list of letters that the user has guessed.
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You have already guessed {guess}")
    
    # Check if the letter the user guessed (guess) is one of the letters in the chosen word
    for position in range(word_length):
        letter = chosen_word[position]
        # In the event the letter is in the word and the player has not guessed it, you can print it in the selected location
        if letter == guess:
            display[position] = letter
    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    from hangman_art import stages
    print(stages[lives])