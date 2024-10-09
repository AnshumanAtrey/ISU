# WAP to read two numbers and arithmetic operator [+,-,*,/,%J perform the operation and display the computed result.
num1=int(input("Enter 1st Number : "))
num2=int(input("Enter 2nd Number : "))
arthOp=input("Enter Arithmetic Operation (*,/,%,+,-) : ")
if arthOp=='+':
    print("Addition : ",num1+num2)
elif arthOp=='-':
    print("Subtraction : ",num1-num2)
elif arthOp=='*':
    print("Multiplication : ",num1*num2)
elif arthOp=='/':
    print("Division : ",num1/num2)
elif arthOp=='%':
    print("Modulus : ",num1%num2)
else:
    print("Invalid Arithmetic Operation")