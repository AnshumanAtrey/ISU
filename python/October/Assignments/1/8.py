inputList = input("Enter list of numbers: ").split()
findVal=input("Enter value to find: ")
if findVal in inputList:
    print(f"{findVal} is found in the list.")
else:
    print(f"{findVal} is not found in the list.")