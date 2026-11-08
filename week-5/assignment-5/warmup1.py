# sum with a loop
sum = 0
# range() starts at 1 and ends at 100 not 101 - the end is always exclusive.
for i in range(1, 101):
    sum += i
print(f"the sum is of addin 1 through 100 is: {sum}")