# Write a function greet(name, greeting="Hello") 
# With only a name argument
def greet(name):
    print(name + "!")
greet("Anna")

# With both a name and a custom greeting
def greet(name, greeting="Hello"):
    print(greeting + " " + name + "!")
greet("Anna", "Good morning ")

# With the greeting passed as a keyword argument
def greet(name, greeting="Hello"):
    print(greeting + " " + name + "!")
greet("Anna", greeting="Good morning")