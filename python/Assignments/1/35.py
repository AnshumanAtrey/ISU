inputVal = input("Enter a string: ")
is_palindrome = True  # Assume it is a palindrome until proven otherwise

# Check characters from start and end moving towards the center
for i in range(len(inputVal) // 2):
    if inputVal[i] != inputVal[len(inputVal) - 1 - i]:
        is_palindrome = False  # Set flag to False if a mismatch is found
        break  # No need to check further if a mismatch is found

if is_palindrome:
    print("Is palindrome")
else:
    print("Not palindrome")