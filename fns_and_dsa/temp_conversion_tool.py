temperature = float(input("Enter the temperature to convert: "))
conversion = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global temperature
    global conversion
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    calculation = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{temperature} is {calculation}°C")


def convert_to_fahrenheit(celsius):
    global temperature
    global conversion
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    
    calculation = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{temperature} is {calculation}°F")
    


if conversion == "C":
    convert_to_fahrenheit(temperature)
else:
    convert_to_celsius(temperature)