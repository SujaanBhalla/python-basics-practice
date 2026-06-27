# DAY 7 - LECTURE 52: DAY 7 GOALS
# Goal:
# Build the Hangman Game.

# Topics:
# - Flow Charts
# - Random Module
# - Lists
# - Strings
# - Loops
# - Functions

# Final Project:
# Hangman Game

# Lecture : 53
# Topic : Hangman Project - Flow Chart
# What is a Flow Chart?
# A Flow Chart is a diagram that shows the step-by-step
# logic of a program before writing the actual code.

# Why use a Flow Chart?
# - Breaks a complex problem into smaller steps.
# - Makes coding easier.
# - Helps understand program logic.
# - Reduces errors while coding.

# Hangman Game Flow

# Step 1
# Generate a random word.

# Example:
# mouse

# Step 2
# Create blanks according to the number of letters.

# Example:
# _ _ _ _ _

# Step 3
# Ask the user to guess a letter.

# Example:
# Guess a letter: o

# Step 4
# Check whether the guessed letter is in the word.

# If YES
# Replace the blank with the correct letter.

# Example:
# _ o _ _ _

# If NO
# The player loses one life.

# Step 5
# Check whether all blanks are filled.

# If YES
# Player Wins.

# If NO
# Continue guessing letters.

# Step 6
# Check remaining lives.

# If lives > 0
# Continue the game.

# If lives == 0
# Game Over.


# Programming Concepts Used

# Random Module
# Strings
# Lists
# Variables
# If-Else
# For Loop
# While Loop
# Functions


# Key Learning

# Before writing code:
# 1. Understand the problem.
# 2. Break it into small steps.
# 3. Draw a Flow Chart.
# 4. Start coding.

# This approach makes coding easier and more organized.

LECTURE 54
# Step 1: Picking a Random Word and Checking Answers
# Objective:
# Build the first part of the Hangman game.

# Steps:
# 1. Randomly choose a word from a list.
# 2. Ask the user to guess a letter.
# 3. Convert the guess to lowercase.
# 4. Check if the guessed letter exists in the chosen word.

# New Concepts:
# - random.choice()
# - String looping using for loop
# - String method: .lower()

# Functions Used:
# random.choice(sequence) -> Returns a random item.
# input() -> Takes user input.
# .lower() -> Converts text to lowercase.

# ==========================================
# DAY 7 - LECTURE 55
# Step 2: Replacing Blanks with Guesses
# ==========================================

# Objective:
# Display guessed letters and hide remaining letters.

# New Concepts:
# - Placeholder String
# - len()
# - Display Variable
# - String Building using +=

# Steps:
# 1. Create blanks (_) equal to word length.
# 2. Replace correct guesses with letters.
# 3. Keep remaining letters as "_".

# Functions Used:
# len()
# range()
# +=


#LECTURE 56: STEP 3 - CHECKING IF THE PLAYER HAS WON
# New Concepts:
# - while loop
# - game_over flag
# - correct_letters list
# - Continue guessing until the word is complete.

# game_over:
# Controls when the game should stop.
# False -> Game continues
# True  -> Game ends

# while not game_over:
# Repeats the game until the player wins.

# correct_letters:
# Stores all correctly guessed letters.
# Prevents previous correct guesses from disappearing.

# display:
# Shows guessed letters.
# Shows "_" for unguessed letters.

# Win Condition:
# if "_" not in display:
#     print("You Win!")
#     game_over = True

# Example:
# Word  : "banana"
# Guess : b -> "b_____"
# Guess : a -> "ba_a_a"
# Guess : n -> "banana"
# Output: You Win!

# LECTURE 57 - STEP 4: KEEPING TRACK OF PLAYER'S LIVES
# Goal:
# Add player lives and display Hangman stages.

# New Concepts:
# - lives Variable
# - Decrement Operator (-=)
# - ASCII Art using List
# - Lose Condition

# Syntax:
# Initial Lives
lives = 6
# Reduce life after wrong guess
if guess not in chosen_word:
    lives -= 1
# Lose Condition
if lives == 0:
    game_over = True
    print("You Lose!")
# Display Current Hangman Stage
print(stages[lives])

# Key Points:
# - Player starts with 6 lives.
# - Wrong guess decreases lives by 1.
# - Game ends when lives become 0.
# - stages[lives] prints the correct Hangman drawing.

# LECTURE 58: STEP 5 - IMPROVING THE USER EXPERIENCE
# Goal:
# Improve the Hangman game by adding user-friendly
# messages and importing data from external modules.

# New Concepts:
# - Python Modules
# - from ... import ...
# - Multiple Imports
# - User Feedback
# - F-Strings

# Syntax:

# Import Specific Variables
from hangman_words import word_list
from hangman_art import stages, logo

# Display Logo
print(logo)

# Check if letter already guessed
if guess in correct_letters:
    print(f"You've already guessed {guess}")

# Wrong Guess
if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word. You lose a life.")

# Display Remaining Lives
print(f"You have {lives}/6 lives left.")

# Show Correct Word
print(f"The correct word was {chosen_word}")

# Key Points:
# - Use modules to organize code.
# - Import only required variables.
# - Give clear feedback to the user.
# - F-Strings make output more readable.
# - Good user experience makes games enjoyable.

# LECTURE 59: THE BENEFITS OF DAILY PRACTICE

# Goal:
# Understand the importance of consistency while learning programming.

# Key Learnings:
# - Practice coding every day.
# - Don't worry if one "day" takes multiple days.
# - Consistency is more important than speed.
# - Learning is a gradual process.
# - Revision and repetition improve understanding.

# Motivation:
# - Keep showing up.
# - Follow the course in order.
# - Small daily progress leads to big results.
# - Trust the learning process.
# - Never compare your pace with others.

# Quote:
# "Consistency beats intensity."
