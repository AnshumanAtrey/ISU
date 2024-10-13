val1=input("Enter a string : ")
print("String with no duplicate characters : ", str(set(val1)))

val2 = input("Enter a string: ")
unique_chars = ""
for char in val2:
    if char not in unique_chars:
        unique_chars += char
print("String with no duplicate characters:", unique_chars)