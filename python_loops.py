# Lecture 37 - Day 5 Goals

# Day 5 Topics:
# - For Loops
# - range() Function
# - Iteration
# - Looping Through Lists

# Day 5 Project:
# Password Generator

# Password Generator Features:
# - Random Letters
# - Random Numbers
# - Random Symbols
# - Strong & Secure Passwords

# Why Strong Passwords?
# - Prevents password reuse attacks
# - Improves account security
# - Makes hacking more difficult

# Learned:
# Today's goal is to learn loops and build a Password Generator.

# Lecture 38 - Using for Loop with Lists
# for loop:
# Used to repeat a block of code multiple times.
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
# Output:
# Apple
# Peach
# Pear
# Using multiple statements inside loop
for fruit in fruits:
    print(fruit)
    print(fruit + "Pie")

# Learned:
# for -> Starts a loop
# in -> Loops through each item
# Loop executes code repeatedly
# Indentation is important

# Lecture 39 - Highest Score
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89]
# sum()
# Returns the total of all numbers in a list.
print(sum(student_scores))
# max()
# Returns the largest number in a list.
print(max(student_scores))
#finding highest score using a for loop
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score 
print(max_score)
# Learned:
# sum() -> Total of numbers
# max() -> Largest value
# for loop -> Iterates through list
# if statement -> Compares values
# Used loop to find highest score manually

# Lecture 40 - for Loops and range()
# range(start, stop)
# Generates numbers from start to stop-1
for number in range(1,11):
    print(number)
# Output:
# 1 2 3 4 5 6 7 8 9 10
# range(start, stop, step)
for number in range(1, 11, 3):
    print(number)
# Output:
# 1 4 7 10
# Sum of Numbers from 1 to 100
total = 0
for number in range(1, 101):
    total += number
print(total)
# Output:
# 5050

# Learned:
# range() generates a sequence of numbers
# stop value is not included
# step controls increment size
# range() is commonly used with for loops
# += is used to accumulate values
# Exercise:
# FizzBuzz
# You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:
# Your program should print each number from 1 to 100 in turn and include number 100.
# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
# e.g. it might start off like this:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# ...etc

for number in range(1, 101):

    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    elif number % 3 == 0:
        print("Fizz")

    elif number % 5 == 0:
        print("Buzz")

    else:
        print(number)
# Day 5 Project - Password Generator

# Learned:
# random.choice() -> Select random item from list
# append() -> Add item to list
# shuffle() -> Randomly reorder list
# for loop -> Generate multiple characters
# Password generated using letters, symbols, and numbers