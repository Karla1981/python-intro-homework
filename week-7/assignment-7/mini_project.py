#  Expense Report Generator
# Use os.path.exists() to verify that ../data/expenses.csv exists before opening it.
import os
import csv
from datetime import datetime

if os.path.exists("../data/expenses.csv"):
    print("../data/expenses.csv found")
else:
    print("File not found.")
    exit()

# Read expenses.csv into a list of dics using vsv.DictReader
with open("../data/expenses.csv", "r") as file:
    records = list(csv.DictReader(file))
    
    for item in records:
        amount = float(item['amount'])
        print(item['category'], item['description'], item['amount'])

# Filter to 'food' category
one_category = [item for item in records if item['category'] == 'Food']


# Calculate the total amount spent on Food
total_amount = sum(float(item['amount']) for item in one_category)
print(f"Food Total Amount: {total_amount:.2f}")

#6. Write a report to food_report.txt
today = datetime.now().strftime("%B %d, %Y")
print(today)

# Using with closes the file as soon as done going over it withouth the need
# of specifying f.close()
with open("food_report.txt", "w", encoding="utf_8") as report:
    report.write(f"Food Expense Report - generated {today}\n")

    for item in one_category:
        date =item['date']
        amount = float(item['amount'])
        report.write(f"{date}: ${amount:.2f}\n")
    report.write(f"Total: ${total_amount:.2f}\n")