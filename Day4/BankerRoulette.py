import random
names_string = input("Provide the names for Banker Roulette: ")
names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

list_len = len(names)

rand_index = random.randint(0, list_len - 1)

name = names[rand_index]

print(f"{name} is going to buy the meal today!")