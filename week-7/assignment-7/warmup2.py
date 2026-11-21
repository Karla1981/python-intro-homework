# Read a CSV with DictReader
import csv

with open('../data/students.csv', 'r') as file:
    reader = csv.DictReader(file)# read file with DictReader
    for row in reader:
        print(row['name'], row['score'])# each row is a list of strings