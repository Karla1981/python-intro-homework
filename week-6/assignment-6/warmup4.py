# Validation Function
def is_valid_score(score):
    if score >= 0 and score <= 100:
        return True 
    else:    
        return False
score = int(input("Enter a score: "))
if is_valid_score(score):
    print("Valid Score.")
else:
    print("Invalid Score - must be between 0 and 100.")

    