# ============================================
# Python Basics Practice
# Topic: Printing to the Console
# Course: 100 Days of Code - Day 1
# Author: Sujaan Bhalla
# ============================================

#Module 1 : lecture 1 to 12

#lecture 1 to 5

print("Hello, World!")
# lecture 6: 

print("\n========== PRINT STATEMENTS ==========\n")
# Printing multiple lines
print("Welcome to Python")
print("I am learning Python")
print("Let's build amazing projects!")

#lecture 6: Practice Ques.
# Recipe Printing Practice
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")

# Same recipe using \n
print("\nUsing a single print statement:\n")

print(
    "1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.\n"
    "2. Knead the dough for 10 minutes.\n"
    "3. Add 3g of Salt.\n"
    "4. Leave to rise for 2 hours.\n"
    "5. Bake at 200 degrees C for 30 minutes."
)

#lecture 7:
print("\n========== STRING CONCATENATION ==========\n")
# Combining strings using +
print("Hello" + " " + "Sujaan")
print("Welcome" + " to " + "Python!")

print("\n========== TRIPLE QUOTES ==========\n")
# Multi-line string using triple quotes
print("""
This is a multi-line string.
It can span multiple lines.
Very useful for long text.
""")

#lecture 7 - practice ques. 
## Fix the code below 👇

# print(Notes from Day 1")
#  print("The print statement is used to output strings")
# print("Strings are strings of characters"
# priint("String Concatenation is done with the + sign")
# print(("New lines can be created with a \ and the letter n")

# Notes from Day 1
# The print statement is used to output strings
# Strings are strings of characters
# String Concatenation is done with the + sign
# New lines can be created with a \ and the letter n
print(
    "Notes from " + "Day 1" + "\n"
    + "The print statement is used to output " + "strings" + "\n"
    + "Strings are strings of " + "characters" + "\n"
    + "String Concatenation is done with the " + "+" + " sign" + "\n"
    + "New lines can be created with a " + "\\" + " and the letter n"
)

# Topic: Python input() Function
prompt_mess = input("Prompt Message")
name = input("What is your name?")

# Using input() with print()
print("Hello" + input("What is your name?"))

# Adding an exclamation mark using string concatenation 
print("Hello " + input("Enter your name: ") + "!")
city = input("Enter your city: ") print("You live in " + city)

# Example Practice 
food = input("Favorite food: ") 
drink = input("Favorite drink: ") 
print("Your favorite combo is " + food + " and " + drink + "!")

# Topic : variable
name = "Sujaan" 
print(name)

# Storing User Input in a Variable
username = input("What is your name? ") 
print("Hello " + username + "!")

# Variables Can Change (Reassignment)
name = "Jack"
print(name)

name = "Angela"
print(name)

# Finding Length of a String using len()
name = "Python"
print(len(name))

#Taking User Input and Finding Length
username = input("Enter your name : ")
length = len(username)

print(length)

# Everything in One Line
print(len(input("What is your name? ")))

#Practice Challenge
city = input("Enter your city: ")
print("You live in" + city)

favoritelanguage = input("Favorite programming language: ")
print("You like " + favoritelanguage)

# Practice Challenge
favorite_food = input("Favorite food: ") 
print("I like " + favorite_food + " too!") 
city = input("City: ") 
print("Welcome from " + city + "!")

#mentor challenge
name = input("What is your name?")
length= len(name)
print("Your name has", length , "characters." )

# Lecture 9: Question Practice
# Variables
# We have 2 variables glass1 and glass2. glass1 contains milk and glass2 
# contains juice. Write 3 lines of code to switch the contents of the 
# variables. You are not allowed to type the words "milk" or "juice". 
# You are only allowed to use variables to solve this exercise.

glass1 = "milk"
glass2 = "juice"

temp = glass1
glass1 = glass2
glass2 = temp

# 1. Use Meaningful Variable Names
n = "Sujaan" # can be better
username = "Sujaan" # give a valid variable

# 2. Multiple Words -> Use Underscore (_)
#correct
user_name = "Sujaan"
student_age = 19
#wrong
user name = "Sujaan"

# 3. Variable Names Can Contain Numbers
# Correct 
student1 = "Rahul"
score2 = 95 

# Wrong (cannot start with a number)
1student = "Rahul" 
2score = 95

# 4. Don't Use Python Keywords or Built-in Function Names 
#Bad Practice 
print = "Hello" 
input = "Python" 
# Better 
message = "Hello" 
user_input = "Python"

# 5. Variable Names Are Case-Sensitive
name = "Sujaan"
Name = "Angela"
print(name) # Sujaan 
print(Name) # Angela

# 6. Be Consistent (Avoid Typos)
username = "Sujaan"
#Correct 
print(username) 
#Wrong (NameError)
print(usernme)

# 7. Good Examples
student_name = "Amit" 
favorite_food = "Pizza" 
total_marks = 480 
city = "Jaipur"

# 8. Bad Examples

a = "Amit"# Too vague
user name = "Amit" # Space not allowed 
1name = "Amit" # Cannot start with a number 
print = "Hello" # Avoid built-in names

# Quiz 1: Examples(Lecture 10)

# Question 1:
# Which line of Python code is valid?
#  Valid 
a = 12
# Invalid 
# var a = 12
# a: 12 
# 12 = a

# Question 2:
# Which is the best variable name for Player 1's username?
# Bad 
# p1 user name = "jackbauer" 
# 1_player_username = "jackbauer" 
# p1u = "jackbauer" 
# Best 
player1_username = "jackbauer"

# Question 3:
# Which block of code will produce an error? For extra points, 
# which type of error do you think it will produce?
time_until_midnight = "5" 
# Wrong 
# print(time_until_Midnight) 
# Because: # time_until_midnight != time_until_Midnight

#lecture 11 : Project created 
# band_name_generator.py

#lecture 12 : 
# 🎉 Congratulations, Sujaan! You have successfully completed Day 1 of the 
# "100 Days of Code" Python course.

# 📚 What you should remember from Day 1
# Topic	Key Idea
# print()	Displays output on the screen
# input()	Takes input from the user
# Variables	Store values for later use
# +	        Concatenates (joins) strings
# \n	    Moves to a new line
# len()	    Counts the number of characters
# Naming	Use meaningful names, underscores, and avoid spaces









