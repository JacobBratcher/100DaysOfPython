# Which number do you want to check?
number = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
calculation = number % 22

# if else statement that determines if the user's number is odd or even
if calculation > 0 : 
    print(f"{number} is odd.")
else :
    print(f"{number} is even.")