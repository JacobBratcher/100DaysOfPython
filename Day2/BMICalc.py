# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input() 
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# weight (lb) / [height (in)]2 x 703

h = float(height)
w = int(weight)

bmi = int(w / (h ** 2))

print(bmi) 