# Warmup4
home_apples = 3
store_apples = int(input("How many apples did you buy: "))
apples = home_apples + store_apples
print(f"You have {apples} apples for the week!" )

# apples = home_apples + store_apples
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# The error is a typeError, what it means is that since I'm asking the user to 
# enter the number of apples bought at the store the program is receiving the number entered
# as a string instead of a number, so for me to be able to perform the mathematical 
# operation I must convert the number to an int and then perform the operation. 4