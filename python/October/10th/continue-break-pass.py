# This program demonstrates the use of continue, break, and pass statements in loops.

# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Iterate over each number in the list
for number in numbers:
    # If the number is 5, skip the rest of the loop and continue with the next iteration
    if number == 5:
        print("Skipping number 5.")
        continue  # Skip the current iteration

    # If the number is 8, break out of the loop entirely
    if number == 8:
        print("Breaking the loop at number 8.")
        break  # Exit the loop

    # If the number is 3, do nothing and move to the next iteration
    if number == 3:
        pass  # Placeholder for future code, does nothing here
    else:
        print(f"Processing number: {number}")

# This line will execute after the loop ends
print("Loop has ended.")
