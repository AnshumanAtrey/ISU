marks1=int(input("Enter marks of first subject: "))
marks2=int(input("Enter marks of second subject: "))
marks3=int(input("Enter marks of third subject: "))
marks4=int(input("Enter marks of fourth subject: "))
marks5=int(input("Enter marks of fifth subject: "))
average=(marks1+marks2+marks3+marks4+marks5)/5
if average>=90:
    print("Grade: A")
elif average>=80:
    print("Grade: B")
elif average>=70:
    print("Grade: C")
elif average>=60:
    print("Grade: D")