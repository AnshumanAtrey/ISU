#Create a module for common mathematical operations and use it in a main program
# math_operations_program.py

# Module for common mathematical operations
def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the quotient of a and b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def power(a, b):
    """Return a raised to the power of b."""
    return a ** b

def modulus(a, b):
    """Return the modulus of a and b."""
    return a % b

# Main program
def main():
    print("Welcome to the Math Operations Program!")
    
    # Example usage of the module functions
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    
    print(f"Addition: {add(a, b)}")
    print(f"Subtraction: {subtract(a, b)}")
    print(f"Multiplication: {multiply(a, b)}")
    
    try:
        print(f"Division: {divide(a, b)}")
    except ValueError as e:
        print(e)
    
    print(f"Power: {power(a, b)}")
    print(f"Modulus: {modulus(a, b)}")

if __name__ == "__main__":
    main()