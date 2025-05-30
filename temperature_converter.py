#5. Temperature Converter: Write a Python program that converts a temperature in Celsius to Fahrenheit.
# Take the Celsius temperature as input from the user.
def celsius_to_fahrenheit(celsius):
    """Formula to convert Celsius to Fahrenheit"""
    return (celsius *9/5)+32
cel_temp = float(input("enter celsius temperature:"))
print("Fahrenheit temparature is: ",celsius_to_fahrenheit(cel_temp))