# Print each key-value pair using .items() in a for loop
student = {"name": "Zoe", 
           "grade": "A", 
           "subjects": ["Math", "English", "Chemistry"]}
# for loop 
for key, value in student.items():
    print(f"{key}: {value}")

# Add a new key "graduated" with the value False
student["graduate"] = False
# Print the updated dictionary
print(f"Student: {student}")