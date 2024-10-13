attempts = 0
while attempts < 5:
    name = input("Enter name: ")
    password = input("Enter password: ")
    if name == "stud" and password == "pass":
        print("Login successful!")
        break
    else:
        print("Invalid credentials. Try again.")
        attempts += 1
if attempts == 5:
    print("Maximum attempts reached.")

