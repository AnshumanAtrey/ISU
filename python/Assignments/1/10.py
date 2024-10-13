num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))

numbers1 = [num1, num2, num3]
numbers1.sort()
print("Numbers in ascending order using sort():", numbers1)

numbers2 = sorted([num1, num2, num3])
print("Numbers in ascending order using sorted():", numbers2)

numbers3 = [num1, num2, num3]
for i in range(len(numbers3)):
    for j in range(i+1, len(numbers3)):
        if numbers3[i]>numbers3[j]:
            numbers3[i], numbers3[j] = numbers3[j], numbers3[i]
print("Numbers in ascending order using for loop:", numbers3)