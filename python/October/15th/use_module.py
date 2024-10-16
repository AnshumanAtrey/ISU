# Importing the entire module
import module_name

# Using the greet function from module_name
greeting = module_name.greet("Alice")
print(greeting)  # Output: Hello, Alice!

# Accessing the variable from module_name
print(module_name.my_variable)  # Output: 42


# Importing the module with an alias
import module_name as m1

# Using the greet function with the alias
greeting_alias = m1.greet("Bob")
print(greeting_alias)  # Output: Hello, Bob!

# Accessing the variable with the alias
print(m1.my_variable)  # Output: 42


# Importing specific items from the module
from module_name import greet, my_variable

# Using the imported function directly
greeting_direct = greet("Charlie")
print(greeting_direct)  # Output: Hello, Charlie!

# Accessing the imported variable directly
print(my_variable)  # Output: 42
