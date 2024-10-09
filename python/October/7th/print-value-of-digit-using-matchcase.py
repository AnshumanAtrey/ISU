#Write a program to take a single digit number from the key board and print its value in English word using match case
singleDigitMatch=int(input("Enter a Digit : "))
match singleDigitMatch:
    case 0:
        print("Zero")
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case 5:
        print("Five")
    case 6:
        print("Six")
    case 7:
        print("Seven")
    case 8:
        print("Eight")
    case 9:
        print("Nine")
    case _:
        print("Number is not a single digit")