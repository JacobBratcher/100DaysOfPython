print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# same as ControlFlow.py, but there is a nested if else statement 
# this statement determines how much the user has to pay based off age
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill =7
        print("Please pay $7.")
    else:
        bill = 12
        print("Please pay $12.")
    
    wants_photo = input("Do you want a photo taken? (Y or N): ")
    if wants_photo == "Y" or "y": 
        #bill = bill + 3 - this is the same as the statement below 
        bill += 3
        
        print(f"Your final bill is ${bill}")
        
else: 
    print("Sorry, you have to grow taller before you can ride.")

    