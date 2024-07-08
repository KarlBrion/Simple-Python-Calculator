def addition(num1, num2):
    """Calculates the sum of two numbers."""
    result = num1 + num2
    return result


def subtraction(num1, num2):
    """Calculates the difference between two numbers."""
    result = num1 - num2
    return result


def multiplication(num1, num2):
    """Calculates the product of two numbers."""
    result = num1 * num2
    return result


def division(num1, num2):
    """Calculates the quotient of two numbers (handles division by zero)."""
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        return None  # Indicate error instead of undefined result
    else:
        result = num1 / num2
        return result
