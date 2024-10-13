import array # Importing the array module
sum_output = 0
# Creating an array of integers
my_array = array.array('i', [1, 2, 3, 4, 5])  # 'i' indicates the type is integer
for i in range(len(my_array)):
    sum_output += my_array[i]
print(sum_output)
