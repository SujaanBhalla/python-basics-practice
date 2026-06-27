# ==========================================
# DAY 7 PROJECT - HANGMAN GAME
# ==========================================

"""
Project Name : Hangman Game
Course       : 100 Days of Code - Python Bootcamp
Day          : 7
Author       : Sujaan Bhalla

Description:
A console-based Hangman game where the player
guesses a hidden word one letter at a time.

Concepts Used:
- Random Module
- Lists
- Strings
- if / else Statements
- for Loops
- while Loops
- Functions
"""

# ==========================================
# PROJECT STARTS HERE
# ==========================================

import random

# ==========================================
# LECTURE 54 - STEP 1: PICKING A RANDOM WORD
# ==========================================

# List of possible words
word_list = [
    "aardvark",
    "baboon",
    "camel"
]

# Randomly choose a word
chosen_word = random.choice(word_list)

# Print chosen word (For Testing)
# print(f"Chosen Word: {chosen_word}")

# Ask the user to guess a letter
guess = input("Guess a letter: ").lower()

# Check each letter
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")


# ==========================================
# LECTURE 55 - STEP 2: REPLACING BLANKS WITH GUESSES
# ==========================================

# Create Placeholder
placeholder = ""

word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"

print(placeholder)

display = ""

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)


# ==========================================
# LECTURE 56 - STEP 3: CHECKING IF THE PLAYER HAS WON
# ==========================================

game_over = False
correct_letters = []
lives = 6

# ==========================================
# LECTURE 57 - STEP 4: KEEPING TRACK OF PLAYER'S LIVES
# ==========================================

# Hangman Stages (ASCII Art)
stages = [
r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
r"""
  +---+
  |   |
      |
      |
      |
      |
=========
"""
]

while not game_over:

    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:

        if letter == guess:
            display += letter
            if letter not in correct_letters:
                correct_letters.append(letter)

        elif letter in correct_letters:
            display += letter

        else:
            display += "_"

    print(display)

    # Wrong Guess
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess}'. That's not in the word.")

        if lives == 0:
            game_over = True
            print("You Lose!")

    # Print Hangman Stage
    print(stages[lives])
    print(f"Lives Left: {lives}")

    # Win Condition
    if "_" not in display:
        game_over = True
        print("You Win!")