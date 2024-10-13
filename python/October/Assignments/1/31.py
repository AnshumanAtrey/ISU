import array 

# Create an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])  # 'i' indicates the type is integer

# Reverse the array by converting it to a list, reversing it, and converting back to an array
reversed_array = array.array('i', arr[::-1])  # Reverse the array

print("Reversed array:", reversed_array)

