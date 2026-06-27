# ==========================================
# DAY 6 PROJECT: ESCAPING THE MAZE
# ==========================================

# Project:
# Guide the robot through any maze using
# the Right-Hand Rule algorithm.

def turn_right():
    turn_left()
    turn_left()
    turn_left()


# Move until a wall is found
while front_is_clear():
    move()

turn_left()


# Follow the right wall
while not at_goal():

    if right_is_clear():
        turn_right()
        move()

    elif front_is_clear():
        move()

    else:
        turn_left()


# ==========================================
# END OF PROJECT
# ==========================================