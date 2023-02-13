def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear() or not wall_in_front():
        move()
    elif wall_in_front() and right_is_clear():
        turn_right()
    elif wall_in_front() and not right_is_clear():
        turn_left()