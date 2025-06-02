def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations based on the given operation.
    
    Parameters:
    num1 (float): First number
    num2 (float): Second number
    operation (str): Type of operation ('add', 'subtract', 'multiply', 'divide')
    
    Returns:
    float or str: Result of the operation or error message for division by zero
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation."
