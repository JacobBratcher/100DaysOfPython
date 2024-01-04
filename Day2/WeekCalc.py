age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

weeks_total = int(4680)

weeks_spent = int(age) * 52

print(weeks_spent)

weeks_left = int(weeks_total - weeks_spent)

print(f"You have {weeks_left} weeks left.")
