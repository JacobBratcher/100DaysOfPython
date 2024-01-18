line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3] # map 1 - index 0, map 2 - index 1, map 3 - index 2
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇 

column = None
row = None

if position[0].lower() == "a":
    row = int(0)
elif position[0].lower() == "b":
    row = int(1)
elif position[0].lower() == "c":
    row = int(2)
else: 
    print("Enter a valid letter (A, B, or C).")

if int(position[1]) >= 0 and int(position[1]) <= 9:
    column = int(position[1]) - 1
else: 
    print("Please enter a number (1-9).")

if column is not None and row is not None:
    map[column][row] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")