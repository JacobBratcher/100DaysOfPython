# simple function
def greet():
    print("Hello Jacob")
    print("How are you doing today?")
    print("Isn't the weather nice today?")
    
# call the function 
greet()

# function that allows for input 
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you doing {name}?")

greet_with_name("Jacob")
greet_with_name("Kayla")

# function with multiple parameters 
def greet_with_names(name1, name2, name3):
    print(f"Hello {name1}, {name2}, and {name3}")
    print(f"How are you doing {name1}, {name2}, and {name3}?")

# calling the function, parameters have to be in order in this positional format
greet_with_names("Jacob", "Hoss", "Frank")

# calling the function, parameters can be set in this keyword argument format 
greet_with_names(name1 = "Jacob", name2 = "Hoss", name3 = "Frank")
