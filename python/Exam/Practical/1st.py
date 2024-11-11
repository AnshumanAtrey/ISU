# Create a simple calculator program using basic operators and functions

# Get user input
x = float(input("First Number: "))  # Convert input to float
op = input("Operator (+, -, *, /): ")  # Get the operator
y = float(input("Second Number: "))  # Convert input to float

# Perform the calculation based on the operator
if op == '+':
    result = x + y
elif op == '-':
    result = x - y
elif op == '*':
    result = x * y
elif op == '/':
    if y != 0:  # Check for division by zero
        result = x / y
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operator"

# Print the result
print("Result:", result)
