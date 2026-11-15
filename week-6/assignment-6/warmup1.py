# Write a function greet(name, greeting="Hello") 
def greet(name, greeting="Hello"):
    print(greeting + " " + name + "!")
# With only a name argument
greet("Anna")
# With both a name and a custom greeting
greet("Anna", "Hi")
# With the greeting passed as a keyword argument
greet("Anna", greeting="Good morning")