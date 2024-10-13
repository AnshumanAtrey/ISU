import array

# Define a predefined array using the array module
arr = array.array('i', [1, 2, 3, 2, 1, 4])  # 'i' indicates the type is integer

# counting elements of array using count
count1=arr.count(1) # Using .count() to count occurrences
print("Element 1 counts:", count1)

# reverse elements of array using .reverse
arr.reverse()
print("Reversed array:", arr)  # Convert to list for better readability

# extend elements from array using .extend
arr2 = array.array('i', [5, 6, 7])  # Predefined array to extend
arr.extend(arr2)
print("Extended array:", arr2)  # Convert to list for better readability
