# Input string from the user
input_string = input("Enter a string: ")

# Split the string into words
words = input_string.split()

# Print words with even length
print("Even length words:")
for word in words:
    if len(word) % 2 == 0:  # Check if the length of the word is even
        print(word)

