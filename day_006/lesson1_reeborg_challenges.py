# The lessons took place on the following site to explore functions: https://reeborg.ca/reeborg.html

# Hurdle 1 code: 
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range(6):
    hurdle()

# Hurdle 2 code:
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# at_goal() is a condition within the game
while not at_goal():
    hurdle()

# Hurdle 3 code:
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# at_goal() and front_is_clear() are conditions in the game:

while not at_goal():
    if front_is_clear() == True:
        move()
    else:
        hurdle()

#  Hurdle 4 code:
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def hurdle():
    turn_left()
    while wall_on_right():     
        move()
    turn_right()
    move()
    turn_right()
    move()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif wall_in_front():
        turn_left()
    elif front_is_clear():
        move()
    else:
        hurdle()

# Maze code:

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move() 
turn_left()  

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()