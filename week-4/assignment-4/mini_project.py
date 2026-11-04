# copied roster.py
students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

# Find the top scorer - 
highest_score = 0 #placeholder
top_scorer = "" # name holder

# loop 
for student in students:
    if student["score"] > highest_score:
        highest_score = student["score"]
        top_scorer = student["name"]
print(f"Top scorer is: {top_scorer} with a score of: {highest_score}")

# Calculate the class avg
total_score = 0
count = 0

for score in students:
    total_score += score["score"]
    count += 1
if count > 0:
    class_avg = total_score / count
    print(f"Class Average: {class_avg}")
else:
    print("hi!")

# List all unique subjects
# initialliaze empty set to remove duplicates
unique_subjects = set()

for subject in students:
    # add the subjects to unique_subjects
    unique_subjects.add(subject["subject"])
print(f"Subjects offered: {unique_subjects}")

# List high scores
high_scorers = []

for student in students:
    if student["score"] > 75:
        high_scorers.append(student["name"])  
print(f"High Scorers: {high_scorers} ")

