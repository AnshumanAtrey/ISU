# Example string
input_string = "Hello, world! Welcome to Python programming."

# Specify the separator we want to partition the string by
separator = "world"

# Use the partition method to split the string
before_separator, found_separator, after_separator = input_string.partition(separator)

# Print the results
print("Original String:", input_string)
print("Separator:", separator)
print("Part before the separator:", before_separator)  # Text before the separator
print("Found Separator:", found_separator)              # The separator itself
print("Part after the separator:", after_separator)      # Text after the separator

