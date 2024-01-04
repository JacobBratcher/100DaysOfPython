# intro
print("Welcome to the tip calculator.")

# accepts user input for total bill 
bill = input("What was the total bill? ")

# accepts user input for tip percentage 
tip_percent = input("What percentage tip would you like to give? 10, 12, or 15? ")

# accepts user input for how many people are spliting the bill
people = input("How many people to split the bill?" )

tip_decimal = int(tip_percent) / 100 

total = (float(bill) * float(tip_decimal)) + float(bill)  

split_total = "{:.2f}".format(float(total) / int(people))

print(f"Each person should pay: {split_total}")