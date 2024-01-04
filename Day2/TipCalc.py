# intro
print("Welcome to the tip calculator.")

# accepts user input for total bill 
bill = input("What was the total bill? ")

# accepts user input for tip percentage 
tip_percent = input("What percentage tip would you like to give? 10, 12, or 15? ")

# accepts user input for how many people are spliting the bill
people = input("How many people to split the bill?" )

# converts whole number given by user input into decimal 
tip_decimal = int(tip_percent) / 100 

# calcualtes total bill with tip 
total = (float(bill) * float(tip_decimal)) + float(bill)  

# splits the bill among how many people the user inputs 
split_total = "{:.2f}".format(float(total) / int(people))

# prints how much each person has to pay 
print(f"Each person should pay: {split_total}")