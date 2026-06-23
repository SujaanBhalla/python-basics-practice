# ==========================================================
# 📚 DAY 2 PROJECT - TIP CALCULATOR
# ==========================================================

#Project
# Create a Tip Calculator,
#REquirements
# 1. Ask the user for the total bill amount. 
# 2. Ask the user for the tip percentage. 
# 3. Ask how many people are splitting the bill. 
# 4. Calculate the total bill including the tip. 
# 5. Divide the bill equally among all people. 
# 6. Round the final amount to 2 decimal places.

# Concepts Used: # ✅ Input Function # ✅ Variables # ✅ Data Types # ✅ Type Conversion # ✅ Mathematical Operations # ✅ round() # ✅ f-Strings

print("Welcome to the Tip Calculator!")

# Get Bill Amount
bill = float(input("What was the total bill? $"))

# Get Number of People
people = int(input("How many people to split the bill? "))

# Convert Percentage to Decimal
tip_as_percent = tip / 100

# Calculate Tip Amount
total_tip_amount = bill * tip_as_percent
# Calculate Total Bill
total_bill = bill + total_tip_amount

# Calculate Per Person Share
bill_per_person = total_bill / people

# Round to 2 Decimal Places
final_amount = round(bill_per_person, 2)

# Display Result
print(f"Each person should pay: ${final_amount}")

# ==========================================================
# EXAMPLE
# ==========================================================
#
# Bill: 124.56
# Tip: 12
# People: 7
#
# Output:
# Each person should pay: $19.93
#
# ==========================================================
# NOTES
# ==========================================================
#
# float()  -> Converts value to decimal number
# int()    -> Converts value to integer
# round()  -> Rounds number
# f""      -> f-string for inserting variables
#
# Formula:
#
# tip_as_percent = tip / 100
#
# total_tip_amount = bill * tip_as_percent
#
# total_bill = bill + total_tip_amount
#
# bill_per_person = total_bill / people
#
# final_amount = round(bill_per_person, 2)
#
# ==========================================================
# END OF DAY 2 PROJECT
# ==========================================================
