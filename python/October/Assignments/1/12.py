num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
operator=input("Enter arithmetic operator: ")
if operator=='+':
    answer=num1+num2
elif operator=='-':
    answer=num1-num2
elif operator=='*':
    answer=num1*num2
elif operator=='/':
    answer=num1/num2
elif operator=='%':
    answer=num1%num2
print(f"The result is {answer}")