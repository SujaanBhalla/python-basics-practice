# ============================================
# Python Basics Practice
# Topic: Data types
# Course: 100 Days of Code - Day 2
# Author: Sujaan Bhalla
# ============================================

#Module 2: lec 13 to 19
# Lecture 13 Notes:
# Today I learned that Day 2 focuses on data types, numbers,
# mathematical operations, type conversion, f-strings, and
# building a Tip Calculator project.

# lecture 14
#String(str)
print("Hello") 
print("123") # This is a STRING, not a number.

# 2. len() works with strings 
print(len("Hello")) 
# Output: 5 
# ❌ This gives a TypeError because 123 is an integer. 
# print(len(123))

# 3. String Indexing (Subscript)
print("Hello"[0]) # H 
print("Hello"[1]) # e 
print("Hello"[4]) # o

# # Negative indexing starts from the end. 
print("Hello"[-1]) # o 
print("Hello"[-2]) # l

# 4. String Concatenation
print("123" + "345")  # Output: # 123345

# 5. Integers (int)
print(123 + 345)  # Output: # 468

# 6. Floating Point Numbers (float)
# Numbers with decimal points. 
pi = 3.14159 
print(pi) 
price = 99.99 
print(price)

# 7. Boolean (bool)
# Boolean values can only be True or False. 
is_student = True 
is_logged_in = False 
print(is_student) 
print(is_logged_in)

# 🚀 MINI PRACTICE
print("Python"[0]) # P 
print("Python"[-1]) # n 
print(100 + 200) # 300 
print("100" + "200") # 100200


#lecture 4: Quiz 2
# Question 1:
# Which statement below is incorrect?
# ❌ "False" is a Boolean 
# ✅ Answer: # "False" is actually a STRING because it is enclosed in quotes. 
# A Boolean value should be written without quotes: 
# False 
# Example: print(type("False")) 
# <class 'str'> print(type(False)) 
# <class 'bool'>

# Question 2: 
# What is the data type of the mystery variable? 
# mystery = 734_529.678 mystery = 734_529.678 
# ✅ Answer: # The data type is FLOAT because it contains a decimal point. 
print(type(mystery)) # <class 'float'>


#Question 3:
# What will the following code print?
street_name = "Abbey Road" 
print(street_name[4] + street_name[7]) 
# Index positions: 
# A b b e y R o a d 
# 0 1 2 3 4 5 6 7 8 9 
# street_name[4] = "y" 
# street_name[7] = "o" 
# ✅ Output: # yo

#Lecture 15:
# 1. TypeError Example
# len() works with strings, not integers. 
print(len("Hello")) # ✅ Output: 5 
# ❌ This will cause a TypeError:  
print(len(123))

# 2. Type Checking using type() 

print(type("Hello")) # <class 'str'> 
print(type(123)) # <class 'int'> 
print(type(3.14)) # <class 'float'> 
print(type(True)) # <class 'bool'>

# 3. Type Conversion (Type Casting)
# Convert string to integer 
print(int("123") + int("456")) # Output: 579 
# Convert integer to string 
age = 20 
print("Age: " + str(age))
# Convert integer to float 
print(float(10)) # 10.0 
# Convert float to integer 
print(int(3.99)) # 3

# 4. String vs Integer
print("123" + "456") # 123456 (Concatenation) 
print(123 + 456) # 579 (Addition)

# 5. ValueError Example
# ❌ Cannot convert letters to an integer. 
# print(int("ABC"))

# 6. Fixing TypeError with str()
name = input("Enter your name: ") 
length = len(name) 
print("Number of letters in your name: " + str(length))

# 📝 KEY NOTES
# ✅ type() -> Checks the data type of a value. 
# ✅ int() -> Converts to integer. 
# ✅ float() -> Converts to float. 
# ✅ str() -> Converts to string. 
# ✅ bool() -> Converts to boolean. 
# Common Errors: 
# • TypeError -> Wrong data type used. 
# • ValueError -> Invalid value for conversion.
# Example: 
# int("123") -> ✅ 123 
# int("ABC") -> ❌ ValueError

#LECTURE 16: MATHEMATICAL OPERATIONS
# 1. Addition (+)
print(7 + 3) # Output: 10

#2. Subtraction (-)
print(7-3) #Output: 4

#3. Multiplication (*)
print(3*2) #Output: 6

#4. Division(/)
print(6/3) #Output: 2.0
print(type(6/3)) #<class 'float'>

# 5. Floor Division (//)
# Removes the decimal part. 
print(5 // 3) # Output: 1 
print(type(5 // 3)) # <class 'int'>

# 6. Exponent (**)
# Raises a number to a power. 
print(2 ** 2) # Output: 4 
print(2 ** 3) # Output: 8

# 7. Order of Operations (PEMDAS) 
# ---------------------------------------------------------- 
# # P -> Parentheses 
# # E -> Exponents 
# # M -> Multiplication 
# # D -> Division 
# # A -> Addition 
# # S -> Subtraction 
print(3 * 3 + 3 / 3 - 3) # Output: 7.0 
# Using parentheses changes the priority. 
print(3 * (3 + 3) / 3 - 3) # Output: 3.0

# 📝 KEY NOTES
# + -> Addition 
# - -> Subtraction 
# * -> Multiplication 
# / -> Division (returns float) 
# // -> Floor Division (returns integer part) 
# ** -> Exponent (power)

# Python follows PEMDAS for mathematical expressions. 
# Parentheses () have the highest priority.

# 🚀 MINI PRACTICE
print(10 + 5) # 15 
print(10 - 5) # 5 
print(10 * 5) # 50 
print(10 / 5) # 2.0 
print(10 // 3) # 3 
print(5 ** 2) # 25

#BMI Calculator
# The body mass index (BMI) is a measure used in medicine 
# to see if someone is underweight 
# or overweight. This is the formula used to calculate it:
# bmi is equal to the person's weight divided by the 
# person's height squared.
# Convert this sentence into code on line 6.

# answer: So complete the code like this:
height = 1.65
weight = 84
# Calculate BMI
bmi = weight / (height ** 2)
print(bmi)

# output : 30

#LECTURE 17: NUMBER MANIPULATION & F-STRINGS
# 1. Original Number
bmi = 30.85399449035813 
print("Original BMI:", bmi)

# 2. Convert to Integer using int()
# int() removes the decimal part (flooring). 
print("Integer BMI:", int(bmi)) # 30

# 3. Round a Number using round()
print("Rounded BMI:", round(bmi)) # 31 
print("Rounded to 2 decimal places:", round(bmi, 2)) # 30.85

# 4. Assignment Operators
score = 0 
print("Initial Score:", score) 
score += 1 
print("After += 1:", score) 
score -= 1 
print("After -= 1:", score) 
score *= 5 
print("After *= 5:", score) 
score /= 2 
print("After /= 2:", score)

# 5. f-Strings
score = 100 
height = 1.75 

is_winning = True 
print(f"Score: {score}") 
print(f"Height: {height}") 
print(f"Winning Status: {is_winning}") 
print(f"Your score is {score}, your height is {height}, and winning is {is_winning}.")

# 6. Without f-Strings (Old Method)
print("Your score is " + str(score))

# 📝 KEY NOTES
# int(x) -> Removes decimal part. 
# round(x) -> Rounds to nearest whole number. 
# round(x, 2) -> Rounds to 2 decimal places. 
# += -> Add and assign 
# -= -> Subtract and assign 
# *= -> Multiply and assign 
# /= -> Divide and assign 
# f"Hello {name}" -> Inserts variables into strings easily.

# 🚀 MINI PRACTICE
marks = 95 
attendance = 92.5 
passed = True 
print(f"Marks: {marks}") 
print(f"Attendance: {attendance}") 
print(f"Passed: {passed}")

# Mathematical Operations Quiz
# Quiz 3|3 questions
# We've covered a lot of mathematical operations you can do with Python. e.g. round(), floor division //, PEMDAS etc. This quiz is going to check to see if you can use all these concepts correctly.

# Question 1:
# You are a computer. What will this line of code print?
# print(6 + 4 / 2 - (1 * 2))
# Using PEMDAS:
# 4 / 2 = 2.0
# 1 * 2 = 2
# 6 + 2.0 - 2
# = 6.0
# ✅ Answer: 6.0
# Question 2
# a = int("5") / int(2.7)
# Step by step:
# int("5") = 5
# int(2.7) = 2
# 5 / 2 = 2.5
# Since / always returns a float:
# type(2.5)
# ✅ Answer: float
# Question 3
# Which line gives an error?
# Option 1
# name = input("What is your name?")
# print(f"Hello, {name}")
# ✅ Correct
# Option 2
# name = input("What is your name?")
# print("Hello, " + name)
# ✅ Correct
# Option 3
# age = 12
# print(f"You are {age} years old")
# ✅ Correct
# The error option is the one not visible in the screenshot, and in Angela's quiz it is usually:
# age = 12
# print("You are " + age + " years old")
# ❌ Error because you cannot concatenate a string and an integer directly.


#lecture 18
# Created Project 2: Tip Calculator ✅

# Learned:
# - User Input
# - Type Conversion
# - Mathematical Operations
# - round()
# - f-Strings

# ==========================================================
# 🎉 DAY 2 COMPLETED
# LECTURE 19: YOU ARE ALREADY IN THE TOP 50%
# ==========================================================

# Day 2 Status: COMPLETED ✅

# Topics Learned:
# ✅ Primitive Data Types
# ✅ Strings
# ✅ Integers
# ✅ Floats
# ✅ Booleans
# ✅ Type Checking
# ✅ Type Conversion
# ✅ Mathematical Operations
# ✅ Number Manipulation
# ✅ Assignment Operators
# ✅ F-Strings

# Coding Exercises Completed:
# ✅ Data Types Quiz
# ✅ BMI Calculator
# ✅ Mathematical Operations Quiz

# Projects Completed:
# ✅ Tip Calculator

# Key Takeaways:
# 1. Python has different data types.
# 2. Numbers can be manipulated using operators.
# 3. Data types can be converted using int(), float(), str().
# 4. f-Strings make output formatting easier.
# 5. Practice and consistency are important.

# Progress Tracker:
# ✅ Day 1 Completed
# ✅ Day 2 Completed

# Next Topic:
# 🚀 Day 3 - Conditional Statements and Logical Operators

# Keep learning.
# Keep building.
# Keep coding.

# ==========================================================
# END OF DAY 2
# ==========================================================


