year=int(input("Enter any year:"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Is a leap year")
else:
    print("Is not a leap year")

