# Input validation with a while loop
while True: # infinite loop...
    try: # check for errors on entered input - whether is a word, or negative int
        positive_num = int(input("Enter a posive number: " ))
        if positive_num > 0:
            break # break here bc is a positive integer
        else:
            print(f"That's not a positive integer. Try again.")
    except ValueError: # if error then ask again
        print(f"That's not a valid integer. Try again.")
print(f"Got it: {positive_num}") # print the positive integer