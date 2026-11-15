# Functions that Return Values
#  Converts Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    convert_celsius_to_fahrenheit = (c * 9/5) + 32
    return convert_celsius_to_fahrenheit
print(f"0 degrees C = {celsius_to_fahrenheit(0):.1f} degrees F")
print(f"100 degrees C = {celsius_to_fahrenheit(100):.1f} degrees F")
print(f"28 degrees C = {celsius_to_fahrenheit(28):.1f} degrees F")

# Converts Fahrenheit to Celsius 
def fahrenheit_to_celsius(f):

    convert_fahrenhiet_to_celsius = (f - 32) * 5/9
    return convert_fahrenhiet_to_celsius
print(f"72 degrees F = {fahrenheit_to_celsius(72):.1f} degrees C")
print(f"66 degrees F = {fahrenheit_to_celsius(66):.1f} degrees C")
print(f"80 degrees F = {fahrenheit_to_celsius(80):.1f} degrees C")