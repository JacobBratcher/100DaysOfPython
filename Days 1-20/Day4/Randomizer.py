import random 
import my_module

random_integer = random.randint(1,10)
print(random_integer)

# variable from another module 
print(my_module.pi)

# how to get a randome float from the random module 
# random.random() provides a float u to .9999
# times the command to expand your options for a random number if needed
random_float = random.random() * 5
print(random_float)

love_score = random.randint (1, 100)
print(f"Your love score is {love_score}")