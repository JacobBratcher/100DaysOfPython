print("Welcome to Treasure Island. \n Your mission is to find the treasure.")
print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                  ''')

direction = input("left or right?: ").lower()
if direction != "left":
    print("Fall into a hole. \n Game Over")
    quit()
status = input("swim or wait?: ").lower()
if status != "wait":
    print("Attacked by trout. \n Game Over.")
    quit()
door_color = input("Which door (pick a color): ").lower()
if door_color == "red":
    print("Burned by the fire. \n Game Over.")
    quit()
elif door_color == "blue":
    print("Eaten by beasts. \n Game Over.")
    quit()
elif door_color != "yellow":
    print("Game Over.")
elif door_color == "yellow":
    print("You Win!")
else:
    print("Game Over.")
    quit()


     