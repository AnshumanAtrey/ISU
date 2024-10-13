rows = int(input("Enter the number of rows: "))
for i in range(rows*2):
    if i<rows:
        print("*"*i)
    else:
        print("*"*(rows*2-i))