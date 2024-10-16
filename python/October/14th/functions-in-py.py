# Function Definition
def greet(name):
    """
    This function takes a name as an argument and prints a greeting message.
    
    Parameters:
    name (str): The name of the person to greet.
    
    Returns:
    None
    """
    # Print a greeting message using the provided name
    print(f"Hello, {name}! Welcome to the program.")

# Function Call
greet("Alice")  # Calling the function with the argument "Alice"

# Another Function Definition
def add_numbers(a, b):
    """
    This function takes two numbers and returns their sum.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    
    Returns:
    int or float: The sum of the two numbers.
    """
    # Calculate the sum of a and b
    return a + b

# Function Call
result = add_numbers(5, 10)  # Calling the function with arguments 5 and 10
print("The sum is:", result)  # Print the result of the addition

# Function with Default Parameter
def multiply_numbers(a, b=2):
    """
    This function multiplies two numbers. The second number has a default value of 2.
    
    Parameters:
    a (int or float): The first number.
    b (int or float, optional): The second number (default is 2).
    
    Returns:
    int or float: The product of the two numbers.
    """
    # Calculate the product of a and b
    return a * b

# Function Call with Default Parameter
default_multiplication = multiply_numbers(5)  # Calls with only one argument
print("Default multiplication result:", default_multiplication)  # Print the result

# Function Call with Both Parameters
custom_multiplication = multiply_numbers(5, 3)  # Calls with both arguments
print("Custom multiplication result:", custom_multiplication)  # Print the result

# Function with Variable Number of Arguments
def concatenate_strings(*args):
    """
    This function concatenates an arbitrary number of strings.
    
    Parameters:
    *args (str): A variable number of string arguments.
    
    Returns:
    str: The concatenated string.
    """
    # Join all the strings in args with a space
    return ' '.join(args)

# Function Call with Multiple Arguments
concatenated_result = concatenate_strings("Hello", "world!", "This", "is", "Python.")
print("Concatenated string:", concatenated_result)  # Print the concatenated result

def return_multiple_values(a, b):
    """
    This function returns multiple values.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    
    Returns:
    tuple: A tuple containing the sum and product of the two numbers.
    """
    # Calculate the sum and product of a and b
    sum_result = a + b
    product_result = a * b
    
    # Return the sum and product as a tuple
    return sum_result, product_result

# Function Call
result_sum, result_product = return_multiple_values(5, 10)  # Calling the function with arguments 5 and 10
print("The sum is:", result_sum)  # Print the sum result
print("The product is:", result_product)  # Print the product result

