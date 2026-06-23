#Project 3 - Treasure Island Project

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