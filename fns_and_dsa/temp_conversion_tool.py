try:
    temperature = input("Enter the temperature to convert: ")
    temperature = float(temperature)
except ValueError:
    raise ValueError("Invalid temperature. Please enter a numeric value.")
    
conversion = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    calculation = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit} is {calculation}°C")

def convert_to_fahrenheit(celsius):
    
    calculation = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius} is {calculation}°F")
    


if conversion == "C":
    convert_to_fahrenheit(temperature)
else:
    convert_to_celsius(temperature)