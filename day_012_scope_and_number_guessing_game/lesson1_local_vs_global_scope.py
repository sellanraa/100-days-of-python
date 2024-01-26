################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local scope - variable created inside a function, only accessible from within function

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# print(potion_strength)

# Global scope

player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()

# Anytime you create a name/namespace, be aware of where it's been created.

# There is no block scope - so variables created in code blocks aren't the same - e.g. if/for loops

# Modifying global scope

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# The above two enemies are actually completely different variables that happen to have the same name - if you want to grab a global variable, you can import it into a function with 'global' keyword

enemies = 1

def increase_enemies():
  global enemies
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Global constants - things that won't change/be modified, should be made in all upper case

PI = 3.14159

