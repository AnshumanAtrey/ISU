import array  # Importing the array module

# Creating an array of integers
my_array = array.array('i', [1, 2, 3, 4, 5])  # 'i' indicates the type is integer

# Adding a single element to the array using append
my_array.append(6)  # Appending the integer 6 to the end of the array

# Adding multiple elements to the array using extend
my_array.extend([7, 8, 9])  # Extending the array by adding multiple integers [7, 8, 9]

# Inserting an element at a specific position using insert
my_array.insert(0, 0)  # Inserting the integer 0 at the beginning (index 0) of the array

# Printing the updated array
print(my_array)  # Output: array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
