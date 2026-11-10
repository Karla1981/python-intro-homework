# FizzBuzz
# loop from 1 - 30 and print one word per line
for number in range(1, 31):
    #print(number)
    if number % 3 == 0 and number % 5 == 0:
        print(f"FizzBuzz")
    elif number % 3 == 0 and number % 5 != 0:
        print("Fizz")
    elif number % 5 == 0 and number % 3 != 0:
        print("Buzz")
    else:
        print(f"{number}")