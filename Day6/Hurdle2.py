# alternative way to approach reborg's world hurdle #2 problem 

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def repeat_turn():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()  

# this while loop will always do the repeat_turn() function 6 times 
# number_of_hurdles = 6 
# while number_of_hurdles > 0:
#     repeat_turn()
#     number_of_hurdles -= 1
#     print(number_of_hurdles)

# this while loop is using the at_goal() condition to determine if the while loop should continue going
# the turn_repeat() function will continue going until the robot has reached the finish flag 
# while at_goal() != True:
#     turn_repeat()

# this while loop does the same as the loop above 
# while not at_goal():
#     turn_repeat()

# use while loops when you don't care what iteration you are in the loop 
# be careful about making infinite while loops 