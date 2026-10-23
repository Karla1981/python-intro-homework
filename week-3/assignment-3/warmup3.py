#Write a script that evaluates the five expressions 
# below and prints each one with its result. 
# Add a comment on each line explaining 
# why the result is what it is:

# not true changes to false AND false = False
# bc using AND is only true when both are TRUE
statement_one = not True and False
print(f"not True and False: {statement_one}") #false

# T or F -- (F and F) AND evaluates first then OR 
# F and F = F or T = T
statement_two = True or False and False
print(f"True or False and False: {statement_two}")#true

# 5  is bigger then 3 is true but the NOT outside changes
# the outcome to flase
statement_three  = not (5 > 3)
print(f"not (5 > 3): {statement_three}")#false

# T and F = f because the not statement is changing the value
# of 4 NOT eqaul 4 to false so t and f = false.
statement_four = 10 == 10 and 4 != 4
print(f"10 == 10 and 4 != 4: {statement_four}")

#not false becomes true and not true becomes false and because they are
# united by an OR the statement becomes TRUE 
statement_five = not False or not True
print(f"not False or not True: {statement_five}")