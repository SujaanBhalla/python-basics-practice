# Day 4 - Lecture 30 & 31
# Random Module
# Random Module:
# Used to generate random values in Python.
# Helpful for games, simulations, passwords, dice rolls, etc.

import random

# randint(a, b)
# Returns a random integer between a and b (inclusive).

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)

# uniform(a, b)
# Returns a random float between a and b.

#coin tosss program
#randint(0,1):
# 0 -> Heads
# 1 -> Tails

coin = random.randint(0,1)

if coin ==0:
    print("heads")
else:
     print("Tails")
# Learned:
# import random -> Imports Random Module
# randint() -> Random Integer
# random() -> Random Float (0 to 1)
# uniform() -> Random Float in a Range
# Used random numbers to build a coin toss program.

# Lecture 32 - Lists

# List:
# A data structure used to store multiple related items.
fruits = ["cherry", "apple", "litchi"]
print(fruits)
# Accessing Items (Indexing)
# Index starts from 0
print(fruits[0]) #cherry
print(fruits[1]) #apple
# Negative Indexing(chooses from bottom )
print(fruits[-1])  #litchi
# Modifying Items
fruits[1] = "Mango"
print(fruits)
# append()
# Adds one item to the end of the list.
fruits.append("Orange")
print(fruits)
fruits.extend(["Banana", "Grapes"])
print(fruits)
# Learned:
# List stores multiple values.
# Index starts from 0.
# Negative index starts from the end.
# append() adds one item.
# extend() adds multiple items.

# Lecture 33 - Who Will Pay The Bill?
import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
"Alice", "Bob", "Charlie", "David", "Emanuel"
# Method 1: random.choice()
person = random.choice(friends)
print(person)
# Method 2: random index
random_index = random.randint(0, 4)
print(friends[random_index])

# Learned:
# random.choice(list) -> Selects a random item from a list.
# random.randint() -> Generates a random index.
# list[index] -> Accesses an item from a list.

# Lecture 34 - IndexError and Nested Lists
fruits = ["Apple", "Banana", "Cherry"]
print(fruits[0])   # Apple
print(fruits[2])   # Cherry

# IndexError
# Happens when index is outside the list range.
# print(fruits[3])   # IndexError

# Nested Lists
# A list inside another list.
vegetables = ["Spinach", "Kale", "Tomato"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

# Learned:
# IndexError -> Index out of range.
# Nested List -> List inside another list.
# len() -> Returns number of items in a list.

#quiz 5 : 
#q1. fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# Answer: fruits[2]
# q2. fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# fruits[-1] = "Melons"
# fruits.append("Lemons")
# print(fruits)
#ans. ["Strawberries", "Nectarines", "Apples", "Grapes",
#  "Peaches", "Cherries", "Melons", "Lemons"]
# ques 3. vegetables =  ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen[1][1])
# Answer: Kale

# Day 4 Project - Rock Paper Scissors

# Concepts Used:
# - Lists
# - Random Module
# - Indexing
# - if / elif / else
# - User Input
# - Game Logic

# Rock Paper Scissors Rules

# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock

# User chooses:
# 0 -> Rock
# 1 -> Paper
# 2 -> Scissors

# Computer generates a random choice.

# Compare choices and decide:
# Win
# Lose
# Draw

# Lecture 36 - Programming is like going to the Gym

# Day 4 Completed ✅

# Key Takeaway:
# Programming is a skill developed through consistent practice.
# The more you code, the better you become.

# Reminder:
# Don't just watch tutorials.
# Write code every day.
# Practice > Theory