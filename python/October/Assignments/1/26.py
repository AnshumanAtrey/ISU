rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    print(chr(64 + i) * i)  # chr(65) is 'A', chr(66) is 'B', etc.

