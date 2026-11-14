def main():
    # copy of numbers from week 5
    numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]#19

    while True:
        option = show_menu()
        if option == 1:
        # call find min function in the if statement
            print(f"The min number is: {find_min(numbers)}")
            print()

        elif option == 2:
            print(f"The max  umber is: {find_max(numbers)}")
        elif option == 3:
            try:
                user_input_num = int(input("Enter a number: "))
                result = search(numbers, user_input_num)
                print(f"Found at index: {result }")
                print()
            except ValueError:
                print("That's not a valid number. Try again.")
                print()
        elif option == 4:
            print(f"The sort list is: {bubble_sort(numbers)}")
        elif option == 5:
            print("Good bye!")
            break
        else:
            print("Invalid score. Please enter a number from 1 to 5.")


#user_input = int(input("Enter an option number from the menu: "))
def show_menu():
    print("==== Number Cruncher ==== ")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    print("Choose an option (1-5): ")
    print("==========================")
    user_input = int(input("Enter an option number from the menu: "))
    return user_input
    
# funtion that finds the minimun number from numbers list
def find_min(numbers):
    min_number = numbers[0]
    for number in numbers:
        if number < min_number:
            min_number = number
    return min_number

# Function that finds the max numbers from numbers list
def find_max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number
    
# Function that searchs for a number and returns the index of it
def search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1

# Function that returns a sorted list - Bubble sort
def bubble_sort(numbers):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True
    return numbers
    
# call main function
if __name__ == "__main__":
    main()