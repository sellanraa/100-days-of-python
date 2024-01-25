# # Review: 
# # Create a function called greet(). 
# # Write 3 print statements inside the function.
# # Call the greet() function and run your code.

# def greet():
#     print("Hello.")
#     print("This is a greet function.")
#     print("Mission accomplished.")

# greet()

# # Function allowing for input

# def greet_with_name(name):
#     print(f"Hello, {name}.")
#     print(f"This is a greet function for {name}.")
#     print("Mission accomplished.")

# greet_with_name("Jack")

# # Functions with more than one input (positional arguments)

# def greet_with(name, location):
#     print(f"Hello, {name}.")
#     print(f"Lovely weather here in {location}, isn't it?")

# greet_with("Jack", "London")

# Functions with more than one input (keyword arguments)

def greet_with(name, location):
    print(f"Hello, {name}.")
    print(f"Lovely weather here in {location}, isn't it?")

greet_with(location="London", name="Jack")