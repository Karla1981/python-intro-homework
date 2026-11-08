# Mini Project
# Copied numbers from numbers.py
numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]#19

# Build a menu-driven program using a while loop.
# while True display the menu optios until it break:
while True:
    print("==== Number Cruncher ==== ")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    print("Choose an option (1-5): ")
    print("==========================")
    
    print()
    user_input = int(input("Enter an integer: "))
    # user input is equal to x
    if user_input == 1:
        # user input = 1 find min
        min_number = numbers[0]
        for number in numbers:
            if number < min_number:
                min_number = number
        print(f"The min number is: {min_number}")
        print()

    elif user_input == 2:
        # user input = 2 find max
        largest_number = numbers[0]
        for number in numbers:
            if number > largest_number:
                largest_number = number
        print(f"The min number is: {min_number}")
        print()

    elif user_input == 3:
        def linear_search(numbers, target):
            for i in range(len(numbers)):
                if numbers[i] == target:
                    print(f"The number is: {target}")
                    return i
            return -1
        result = linear_search(numbers, 8)
        print(f"At index: {result}")
        print()

    # user input = 4 sort the list
    elif user_input == 4:
        def bubble_sort(numbers):
            swapped = True
            while swapped:
                swapped = False
                for i in range(len(numbers) - 1):
                    if numbers[i] > numbers[i + 1]:
                        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                        swapped = True
            return numbers
        print("List sorted implementing bubble sort: ")
        print(bubble_sort(numbers))
        print()

        # user input = 5 quit
    elif user_input == 5:
        break
    else:
        break



        

        

    
