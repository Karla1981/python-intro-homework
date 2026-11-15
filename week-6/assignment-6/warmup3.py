# Scope in Action
# define a var inside a function
def var_inside():
    number = 10
    return number
#print(number)
# NameError: name 'number' is not defined
num = var_inside()
print(num)
