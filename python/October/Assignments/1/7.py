char=input("Enter single character: ")
if len(char)!=1:
    print("Invalid input")
elif char in "aeiouAEIOU":
    print("The character is a vowel.")
else:
    print("The character is a consonant.")