```python
# ==========================================================
# 📚 DAY 3 - LECTURE 20: DAY GOALS
# ==========================================================

# Topics to Learn Today:
# ✅ if Statements
# ✅ else Statements
# ✅ elif Statements
# ✅ Conditional Operators
# ✅ Modulo Operator (%)
# ✅ Nested if Statements
# ✅ Multiple if Statements
# ✅ Logical Operators (and, or, not)

# Day 3 Project:
# 🎮 Treasure Island Game

# Project Goal:
# Create a text-based adventure game where the user
# makes decisions to find a hidden treasure.

# Example Decisions:
# - Go Left or Right
# - Wait or Swim
# - Choose Red, Blue, or Yellow Door

# Learning Outcome:
# By the end of Day 3, I will be able to make programs
# take different actions based on user choices.

# ==========================================================
# DAY 3 STARTED 🚀
# ==========================================================
# ==========================================================
# 📚 DAY 3 - LECTURE 22
# Control Flow with if / else and Conditional Operators
# ==========================================================

# ----------------------------------------------------------
# What is Control Flow?
# ----------------------------------------------------------

# Control Flow allows a program to make decisions.

# Example:
# IF a condition is True:
#     Do one thing
# ELSE:
#     Do another thing

# ----------------------------------------------------------
# Basic if / else Example
# ----------------------------------------------------------

water_level = 50

if water_level > 80:
    print("Drain Water")
else:
    print("Continue Filling")

# Output:
# Continue Filling

# ----------------------------------------------------------
# Roller Coaster Example
# ----------------------------------------------------------

print("Welcome to the Roller Coaster!")

height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the roller coaster.")
else:
    print("Sorry, you have to grow taller before you can ride.")

# ----------------------------------------------------------
# Comparison Operators
# ----------------------------------------------------------

# >   Greater Than
# <   Less Than
# >=  Greater Than or Equal To
# <=  Less Than or Equal To
# ==  Equal To
# !=  Not Equal To

# ----------------------------------------------------------
# Examples
# ----------------------------------------------------------

age = 18

if age >= 18:
    print("You can vote.")

number = 10

if number == 10:
    print("Number is equal to 10")

if number != 5:
    print("Number is not equal to 5")

# ----------------------------------------------------------
# Assignment vs Comparison
# ----------------------------------------------------------

# Assignment Operator
score = 100

# Comparison Operator
print(score == 100)

# Output:
# True

# ----------------------------------------------------------
# Indentation
# ----------------------------------------------------------

# Python uses indentation to define code blocks.

if True:
    print("Inside If Block")

print("Outside If Block")

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

marks = 75

if marks >= 50:
    print("Pass")
else:
    print("Fail")

# Output:
# Pass

# ==========================================================
# 📝 WHAT I LEARNED
# ==========================================================

# 1. if statements
# 2. else statements
# 3. Comparison operators
# 4. Code blocks
# 5. Indentation
# 6. Control flow

# ==========================================================
# DAY 3 - LECTURE 23: MODULO OPERATOR (%)
# ==========================================================

# % returns the remainder after division.

print(10 % 5)   # 0
print(10 % 3)   # 1

# Even Number Check

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# ==========================================================
# WHAT I LEARNED
# ==========================================================

# % -> Modulo Operator
# Returns the remainder after division

# Even Number:
# number % 2 == 0

# Odd Number:
# number % 2 != 0

# ==========================================================
# END OF LECTURE 23
# ==========================================================

# ==========================================================
# DAY 3 - LECTURE 24
# Nested if Statements and elif Statements
# ==========================================================

# Nested if Example

height = 130
age = 15

if height >= 120:
    print("You can ride.")

    if age <= 18:
        print("Pay $7")
    else:
        print("Pay $12")
else:
    print("You cannot ride.")

# ----------------------------------------------------------
# elif Example
# ----------------------------------------------------------

age = 15

if age < 12:
    print("Pay $5")
elif age <= 18:
    print("Pay $7")
else:
    print("Pay $12")

# ==========================================================
# WHAT I LEARNED
# ==========================================================

# Nested if -> if statement inside another if statement.
# elif -> Checks multiple conditions.
#
# Syntax:
#
# if condition:
#     code
# elif condition:
#     code
# else:
#     code

# ==========================================================
# END OF LECTURE 24
# ==========================================================

# ==========================================================
# CODING EXERCISE 5: BMI CALCULATOR WITH INTERPRETATIONS
# ==========================================================

weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")

# Learned:
# ✅ if
# ✅ elif
# ✅ else
# ✅ Multiple conditions

# ==========================================================

# Lecture 25 - Multiple If Statements

bill = 0
age = 21

if age < 12:
    bill = 5
elif age <= 18:
    bill = 7
else:
    bill = 12

wants_photo = "y"

if wants_photo == "y":
    bill += 3

print(f"Your final bill is ${bill}")

# Learned:
# if/elif/else -> Only one condition runs.
# Multiple if -> Every condition is checked.
# += adds to the current value.

# Lecture 26 - Pizza Order Practice

bill = 0

size = "L"
pepperoni = "Y"
extra_cheese = "Y"

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Final Bill: ${bill}")

# Learned:
# Nested if statements
# Multiple if statements
# += operator
# Bill calculation using conditions

# Lecture 27 - Logical Operators

age = 50

if age >= 45 and age <= 55:
    print("Free Ride")

print(10 > 5 and 8 < 10)   # True
print(10 > 5 or 8 > 10)    # True
print(not 10 > 5)          # False

# Learned:
# and -> Both conditions must be True
# or  -> At least one condition must be True
# not -> Reverses True/False
# Quiz 4 - Logical Operators

# Question 1

print(not 5 == 5)

# 5 == 5 → True
# not True → False

# Answer: False ✅


# Question 2

print(False or True or False)

# One True is enough for OR

# Answer: True ✅


# Question 3

a = 5
b = 7

if a >= b and a != b:
    print("A")
elif not a >= b and a != b:
    print("B")
else:
    print("C")

# a >= b → False
# not False → True
# a != b → True

# True and True → True

# Answer: B ✅

# Lecture 28 - Treasure Island Project

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("Left or Right?\n").lower()

if choice1 == "left":

    choice2 = input("Swim or Wait?\n").lower()

    if choice2 == "wait":

        choice3 = input("Red, Yellow or Blue?\n").lower()

        if choice3 == "yellow":
            print("You Win!")

        elif choice3 == "red":
            print("Game Over.")

        elif choice3 == "blue":
            print("Game Over.")

        else:
            print("Game Over.")

    else:
        print("Game Over.")

else:
    print("Game Over.")

# Learned:
# if, elif, else
# Nested conditions
# .lower()
# Input handling
# Decision-based game logic

# Lecture 29 - Share and Show Off Your Project

# Day 3 Completed ✅

# Project Completed:
# Treasure Island

# Key Concepts Learned:
# if, elif, else
# Nested if statements
# Multiple if statements
# Logical operators
# User input
# Conditional logic

# Reminder:
# Make projects your own.
# Add new stories, choices, and endings.
