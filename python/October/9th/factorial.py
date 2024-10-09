n=int(input("Enter any number you want factorial of :"))
fact=1
if n<0:
    print("Factorial does not exist for negative numbers")
elif n==0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,n+1):
        fact*=i
print(f"Factorial of {n} is {fact}")
