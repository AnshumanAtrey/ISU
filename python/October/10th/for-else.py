# This program demonstrates the use of a for loop with an else clause.

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Iterate over each number in the list
for number in numbers:
    # Check if the number is even
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
else:
    # This block executes after the for loop completes without a break
    print("Finished checking all numbers.")
