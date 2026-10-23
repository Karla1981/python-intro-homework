num = int(input("Enter a number: "))
# num is positive
if num > 0:
    print(f"{num} is positive.")
# num is negative
elif num < 0:
    print(f"{num} is negative.")
# num is zero
else:
    print(f"{num} is zero.")
    
# check for even or odd
if num % 2 == 0:
    print(f"{num} is even.")
else: 
    print(f"{num} is odd.")