def simple_calculator():
    first_num = int(input("Enter the first number: "))
    second_num = int(input("Enter the second number: "))
    operator = input("Enter an operation (+, -, *, /): ")

    if operator == '+':
        print(f"{first_num} + {second_num} = {first_num + second_num}")
    elif operator == '-':
        print(f"{first_num} - {second_num} = {first_num - second_num}")
    elif operator == '*':
        print(f"{first_num} * {second_num} = {first_num * second_num}")
    elif operator == '/':
        if second_num != 0:
            print(f"{first_num} / {second_num} = {first_num / second_num}")
        else:
            print("Error: Division by zero.")
    else:
        print("Invalid operation. Please use +, -, *, or /.")

if __name__ == "__main__":
    simple_calculator()

