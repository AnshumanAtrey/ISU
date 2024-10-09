#WAP to check whether a inputted character is uppercase or lowercase or digit or any other character.
inputtedVal=input("Enter Character or Number : ")
ascii_code = ord(inputtedVal)
if 65 <= ascii_code <= 90:
    print("Uppercase letter")
elif 97 <= ascii_code <= 122:
    print("Lowercase letter")
elif 48 <= ascii_code <= 57:
    print("Number")
else:
    print("Special character")