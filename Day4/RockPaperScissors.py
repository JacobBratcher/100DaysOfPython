import random
import time 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to my Rock Paper Scissors game!")
player_choice = int(input("What do you choose? \n Type 0 for Rock, \n 1 for Paper, \n 2 for Scissors. \n"))
player_item = None 

if player_choice == 0: 
    player_item = "Rock"
    print(rock)
elif player_choice == 1:
    player_item = "Paper"
    print(paper)
elif player_choice == 2:
    player_item = "Scissors"
    print(scissors)
else:
    print("Please enter a valid number (0-2).")
    
time.sleep(1)
    
computer_choice = random.randint(0,2)
computer_item = None

print("The computer's choice is: ")

if computer_choice == 0: 
    computer_item = "Rock"
    print(rock)
elif computer_choice == 1:
    computer_item = "Paper"
    print(paper)
elif computer_choice == 2:
    computer_item = "Scissors"
    print(scissors)
    
if computer_choice < player_choice: 
    print(f"You win! {player_item} beats {computer_item}.")
elif player_choice < computer_choice: 
    print(f"You lose! {computer_item} beats {player_item}.")
else:
    print("You tied with the computer, please restart to play again.")
    


