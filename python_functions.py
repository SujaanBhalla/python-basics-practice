# ==========================================================
# DAY 6 - FUNCTIONS & WHILE LOOPS
# ==========================================================

# Lecture 43 - Day 6 Goals

# Topics:
# - Functions
# - Code Blocks
# - Indentation
# - While Loops

# Day 6 Project:
# Escape the Maze

# Project Concepts:
# - Functions
# - while loops
# - Problem Solving
# - Code Reusability

# Learned:
# Today we will learn functions, while loops, and build
# an Escape the Maze project.

# DAY 6 - LECTURE 44 : DEFINING & CALLING PYTHON FUNCTIONS
# What is a Function?
# A function is a reusable block of code that performs a specific task.
# Functions help reduce repetition and make code cleaner.

# Built-in Functions:
print("Hello")
print(len("Python"))
print(type(10))
print(range(5))
# Defining a Function
# Syntax:
# def function_name():
#     code
def greet():
    print("Hello")
    print("Welcome to Python!")
# Calling a Function
greet()

# Output:
# Hello
# Welcome to Python!

# Another Example
def say_bye():
    print("Good Bye!")

say_bye()

# Multiple Statements Inside a Function
def morning_routine():
    print("Wake Up")
    print("Brush Teeth")
    print("Study Python")
morning_routine()

# Why Functions?
print("Hello")
print("Welcome")
print("Hello")
print("Welcome")

# With Function:

def welcome():
    print("Hello")
    print("Welcome")
welcome()
welcome()

# Reeborg's World Example
# Robot Commands:
# move()
# turn_left()
# Create your own function:
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Another Example:
def turn_around():
    turn_left()
    turn_left()

# Function Flow
# Step 1 -> Define Function
# Step 2 -> Call Function
# Step 3 -> Function Executes

# Key Notes


# def        -> Defines a function
# ()         -> Function parentheses
# :          -> Starts function block
# Indentation -> Code belongs to function
# function() -> Calls the function

# Functions improve:
# - Code Reusability
# - Readability
# - Maintainability
# - Reduce Repetition

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

def favorite_language():
    print("Python")

favorite_language()

def greet_user():
    print("Hello Sujaan!")
    print("Keep Coding!")

greet_user()

# DAY 6 - LECTURE 45: HURDLES LOOP CHALLENGE
# Goal:
# Make the robot jump over all hurdles using functions and loops.
#create turn_right() function
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#create jump() function
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# Repeat the jump 6 times
for step in range(6):
    jump()

# Key Notes
# def -> Define a function
# Functions reduce repeated code
# for loop repeats a task
# range(6) runs the loop 6 times

#LECTURE 46: INDENTATION IN PYTHON
# Indentation:
# Indentation defines a block of code in Python.

# Example
def greet():
    print("Hello")
    print("Welcome!")

greet()
# if Statement
age = 18

if age >= 18:
    print("Adult")

# for Loop
for i in range(3):
    print(i)

# Key Notes
# - Python uses indentation to group code.
# - Standard indentation = 4 spaces.
# - Indented code belongs to the function, loop, or condition.
# - Do not mix tabs and spaces.
# - Most editors use the Tab key to insert 4 spaces.

# ✅ Question 1
# Which version of code will
#  produce an Indentation Error?
# ✔️ Answer: Option 2
def my_function():
print("Hello")
# Reason: The print() statement is not indented 
# after the function definition, so Python 
# raises an IndentationError.
# ✅ Question 2
# Which version of code 
# will output "This will run"?
# ✔️ Answer: Option 3
def my_function():
    print("This will run")

my_function()
# Reason: The function is defined correctly and then called,
#  so "This will run" is printed.
# ✅ Question 3
# In which version of code will 
# you see "This will run" printed?
# ✔️ Answer: Option 1
def my_function():
    a = 3
    if a > 2:
        print("This will run")
my_function()
# Reason: a = 3, so the condition 
# a > 2 is True, and the print() statement is 
# correctly indented inside the if block.

# LECTURE 47: WHILE LOOPS
# While Loop
# Repeats code while a condition is True.
# Syntax
count = 5
while count > 0:
    print(count)
    count -= 1
# Reeborg Example
while not at_goal():
    jump()
# Infinite Loop Example (Avoid)
# while True:
#     print("Running...")

# Key Notes
# while -> Starts a while loop
# Runs until condition becomes False
# Update the condition to avoid infinite loops
# Use while when number of repetitions is unknown

#LECTURE 48: HURDLES USING WHILE LOOP
# Goal:
# Make the robot cross randomly placed hurdles.
def turn_right()
    turn_left()
    turn_left()
    turn_left()

def jump()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

# Key Notes
# while -> Repeat until goal is reached
# if -> Check for wall
# jump() -> Jump over hurdle
# move() -> Move when path is clear

#LECTURE 49: VARIABLE HEIGHT HURDLES
# Goal:
# Make the robot jump over hurdles of random heights.

def turn_right()
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()

    while wall_on_right():
        move()

    turn_right()
    move()
    turn_right()

    while front_is_clear():
        move()
    
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

# Key Notes
# while wall_on_right() -> Climb up wall
# while front_is_clear() -> Move down wall
# if wall_in_front() -> Jump
# else -> Move forward
# wall_on_right()
# Returns True if there is a wall on the robot's right.

# front_is_clear()
# Returns True if the path ahead is clear.

# at_goal()
# Returns True when the robot reaches the destination.

#LECTURE 50: ESCAPING THE MAZE
# Goal:
# Guide the robot through any maze using the
# Right-Hand Rule algorithm.
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#Find a wall first
while front_is_clear():
    move()

#Follow the right wall
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    
    elif front_is_clear():
        move()
    
    else:
        turn_left()

# Learned:
# Used the Right-Hand Rule algorithm to solve
# any maze using while loops and conditionals.
# right_is_clear()
# Returns True if the right side is open.

# front_is_clear()
# Returns True if the front path is open.

# at_goal()
# Returns True when the robot reaches the goal.

# Right-Hand Rule
# Keep your right hand on the wall to
# eventually find the maze exit.

#LECTURE 51: KEEP PRACTICING
# Key Takeaways
# Learning programming is difficult at first.
# Struggling means you are learning.
# Practice consistently every day.
# Don't give up when things feel hard.
# Improvement comes with repetition.

# Motivation
# Hard work + consistency > Natural talent

# Learned:
# Programming gets easier with regular practice.
# Mistakes and challenges are part of the learning process.
# Stay consistent and keep coding every day.

# Remember:
# Every expert programmer was once a beginner.
# Keep showing up, keep practicing,
# and trust the learning process.
