val=input("Enter a character or a digit: ")
if val.isupper():
    print("Uppercase letter")
elif val.islower():
    print("Lowercase letter")
elif val.isdigit():
    print("Digit")
else:
    print("Special character")