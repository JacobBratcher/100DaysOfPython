print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# same as ControlFlow.py, but there is a nested if else statement 
# this statement determines how much the user has to pay based off age
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else: 
    print("Sorry, you have to grow taller before you can ride.")

    