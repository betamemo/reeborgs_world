put()
while front_is_clear():
    move()
    if object_here():
        take()
        turn_left()
        turn_left()
        move()
        if object_here():
            break
        else:
            put()
    elif wall_in_front():
        put()
        turn_left()
        turn_left()
        move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
