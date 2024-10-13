# id function in Python
# The id() function returns the identity of an object.
# This identity is unique and constant for the object during its lifetime.

# Example of using the id() function
a = 42
b = a  # b references the same object as a

# Get the id of the object referenced by a
print("The id of a is:", id(a))  # Outputs the unique id of the object 42
print("The id of b is:", id(b))  # Outputs the same id as a, since b references the same object

# Changing the value of a
a = 100  # Now a references a new object

print("The id of a after change is:", id(a))  # Outputs a new id
print("The id of b remains the same:", id(b))  # Outputs the same id as before

# Explanation of how id() works in hardware
# In Python, every object is stored in memory, and the id() function returns the memory address of the object.
# This address is where the object is stored in the computer's RAM.
# When an object is created, Python allocates a block of memory for it and assigns an identifier (memory address).
# When the object is deleted or goes out of scope, the memory can be reclaimed by Python's garbage collector.
