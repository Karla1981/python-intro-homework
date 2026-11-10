# Linear Search
# Hardcoded name list
names = ["Anna", "Zoe", "Mila", "Blue", "May", "June"]

#  Ask the user to enter a name
user_input = input("Enter a name: ")

# Loop through the list and print whether the name was 
# found and at what index
found = False
index_name = 0
for name in names:
    if name == user_input:
        found = True
        break
    index_name +=1
if found:
    print(f"Found {user_input} at index {index_name}")
else:
    print(f' "{user_input}" was not found in the list')