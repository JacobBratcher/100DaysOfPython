import random

# step 1 

word_list = ["ardvark", "baboon", "camel"]

# to-do 1: randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)

# to-do 2: ask the user to guess a letter and assign their answer to a variable guess. make the guess lowercase.

guess = input("Guess a letter to see if it is in the chosen word: ").lower()

# to-do 3: check if the letter the user guessed (guess variable) is one of the letters in the chosen word. 
# to-do 4: create a while loop that loops until every letter of the chosen word is guessed correctly

correct_guesses = 0

while correct_guesses < len(chosen_word):
    guess = input("Guess a letter to see if it is in the chosen word: ").lower()
    if guess in chosen_word:
        print("Correct! The letter is in the chosen word.")
        chosen_word = chosen_word.replace(guess, "_")
        correct_guesses += 1
    else:
        print("Wrong! The letter is not in the chosen word.")

