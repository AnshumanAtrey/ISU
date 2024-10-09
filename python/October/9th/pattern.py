rows = int(input("Enter the number of rows: "))
for i in range(1, rows+1):
    print("*" * i)
for i in range(1, rows+1):
    for j in range(i):
        print(chr(65+j), end=" ")
    print()
i = 1
while i <= rows:
    print("*" * i)
    i += 1
i = 1
while i <= rows:
    j = 0
    while j < i:
        print(chr(65+j), end=" ")qs
        j += 1
    print()
    i += 1



