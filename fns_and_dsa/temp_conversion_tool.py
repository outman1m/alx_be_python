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
        temp = float(input("Enter temperature: "))
        unit = input("Celsius or Fahrenheit? (C/F): ").upper()
        
        if unit == 'F':
            print(f"{temp}°F = {convert_to_celsius(temp):.2f}°C")
        elif unit == 'C':
            print(f"{temp}°C = {convert_to_fahrenheit(temp):.2f}°F")
        else:
            print("Error: Please enter C or F")
    except ValueError:
        print("Error: Invalid number")

if __name__ == "__main__":
    main()
