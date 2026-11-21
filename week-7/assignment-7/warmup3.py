# Use the os module
import os
print(os.getcwd())

# check if file exist
if os.path.exists("../data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv file not found.")

# 3 - Use os.path.join() tobuild the path
path = os.path.join("..", "data", "expenses.csv")
print(path)
