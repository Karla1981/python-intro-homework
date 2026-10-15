#Temperature converter
fahrenheit = float(input("Please enter a temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"Fahrenheit: {fahrenheit} degres F is {celsius:.1f} degrees C")