def greet(**kwargs):
    """
    This function takes a variable number of keyword arguments and prints a greeting message.
    
    Parameters:
    **kwargs (dict): A dictionary of keyword arguments.
    
    Returns:
    None
    """
    if 'name' in kwargs:
        print(f"Hello, {kwargs['name']}!")
    else:
        print("Hello, stranger!")

# Example usage:
greet(name="Alice")  # Output: Hello, Alice!
greet()  # Output: Hello, stranger!