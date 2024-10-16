#positional argument
def greet(name):
    print(f"Hello, {name}!")

#keyword argument
def greet(name, message="Welcome to the program."):
    print(f"Hello, {name}! {message}")

def greet(name, message="Welcome to the program."):
    print(f"Hello, {name}! {message}")

greet("Alice")  # Calling the function with positional argument
greet(name="Bob")  # Calling the function with keyword argument
greet("Charlie", "Good morning!")  # Calling the function with both positional and keyword arguments

# Default Argument Explanation

# In Python, a default argument is a value that is assigned to a function parameter if no argument is provided when the function is called. This allows the function to have a default behavior when certain parameters are not explicitly specified.

# The following function `greet` takes two parameters: `name` and `message`. The `message` parameter has a default value of "Welcome to the program." assigned to it. This means that if the `message` parameter is not provided when calling the function, it will default to "Welcome to the program.".

def greet(name, message="Welcome to the program."):
    print(f"Hello, {name}! {message}")

# Example usage:

# Calling the function with only the name parameter will use the default message
greet("Alice")
# Output: Hello, Alice! Welcome to the program.

# Calling the function with both name and message parameters will override the default message
greet("Bob", "Good morning!")
# Output: Hello, Bob! Good morning!

# Note that default arguments are evaluated only once at the point of function definition in the defining scope. This means that if you use a mutable default argument and mutate it, you will and have mutated that object for all future calls to the function as well.

# For example, if we define a function with a default argument as a list, and we append to that list within the function, it will affect all future calls to the function:

def append_to_list(value, list=[]):
    list.append(value)
    return list

print(append_to_list(1))  # Output: [1]
print(append_to_list(2))  # Output: [1, 2]
print(append_to_list(3))  # Output: [1, 2, 3]

# To avoid this issue, it's better to use None as the default argument and initialize the mutable object inside the function:

def append_to_list(value, list=None):
    if list is None:
        list = []
    list.append(value)
    return list

print(append_to_list(1))  # Output: [1]
print(append_to_list(2))  # Output: [2]
print(append_to_list(3))  # Output: [3]

#variable argument
def greet(*names):
    for name in names:
        print(f"Hello, {name}!")