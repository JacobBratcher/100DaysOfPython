# how to print to the console 
print("Hello World!")

# lesson 1 
print('Day 1 - Python Print Function')

print('The function is declared like this:')

# can make sentence or word a string and print to console like this 
sentence3 = '''print('what to print')'''
print(sentence3)

# print on a new line in the same statement 
# the \n acts a space and does not neet any gaps
print("This is on one line\nand this is on a different line")

# combine two strings 
# could also be two variables, + combines 
print("Hello, I am string 1 " + "and I am string 2")

# input statements are used to get input from the user 
input("What is your name?: ")

# you can combine print and input statements
# this will ask the input prompt first then complete the "Hello, Jacob" assuming that you put Jacob into the input prompt 
print("Hello, " + input("what is your name?: ")) 

# this is how you can retrive a string and count the amount of characters in said string 
name = input("What is your name, so that I can count the amount of letters that are in it: ")
count = len(name)
print(count)