import array  # Importing the array module

# Creating an array of integers
my_array = array.array('i', [1, 2, 3, 4, 5, 6, 7])  # 'i' indicates the type is integer

# Removing an element using pop
popped_element = my_array.pop()  # Removes and returns the last element (7) from the array
print(f"Popped element: {popped_element}")  # Output: Popped element: 7

# Removing an element using remove
my_array.remove(3)  # Removes the first occurrence of the integer 3 from the array

# Removing an element using del
del my_array[0]  # Deletes the element at index 0 (which is now 1 after the previous removal)

# Printing the updated array
print(my_array)  # Output: array('i', [2, 4, 5, 6])
