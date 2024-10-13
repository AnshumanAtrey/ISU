import array

# Original array with duplicates
arr = array.array('i', [1, 2, 3, 2, 4, 5, 1])  # 'i' indicates the type is integer

# Remove duplicates by converting to a set and back to an array
unique_array = array.array('i', set(arr))  # Create a new array from the set of unique elements

# Print the unique array
print("Array with duplicates removed:", unique_array.tolist())  # Convert to list for better readability

