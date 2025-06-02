# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FREEZING_POINT_OFFSET = 32

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - FREEZING_POINT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + FREEZING_POINT_OFFSET

def main():
    print("Temperature Conversion Tool")
    try:
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
        
        if unit == 'F':
            result = (temp - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
            print(f"{temp}°F is {result:.2f}°C")
        elif unit == 'C':
            result = temp * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
            print(f"{temp}°C is {result:.2f}°F")
        else:
            print("Error: Invalid unit. Please enter 'C' or 'F'.")
    except ValueError:
        print("Error: Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
