import random
import string

print("Welcome to the PyPassword Generator!")
letters = int(input("How many letters would you like to use in your password? "))
symbols = int(input("How many symbols would you like? "))
numbers = int(input("How many numbers would you like? "))

password_characters = []

for _ in range(letters):
    password_characters.append(random.choice(string.ascii_letters))

for _ in range(symbols):
    password_characters.append(random.choice(string.punctuation))

for _ in range(numbers):
    password_characters.append(random.choice(string.digits))

random.shuffle(password_characters)

password = ''.join(password_characters)

print(f"Here is your password: {password}")

