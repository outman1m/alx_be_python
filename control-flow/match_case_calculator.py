#!/usr/bin/python3
# Using if/elif because Python 3.8 doesn't support match case (needs 3.10+)
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ").strip()

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("Cannot divide by zero")
        exit()
    result = num1 / num2
else:
    print("Invalid operation")
    exit()

print(f"The result is {result}")
