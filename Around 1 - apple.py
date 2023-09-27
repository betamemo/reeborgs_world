move()
while not at_goal():
    if wall_in_front():
        turn_left()
    if object_here("apple"):
        take()
    move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
