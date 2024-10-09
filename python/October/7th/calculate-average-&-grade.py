# WAP to calculate to take in the marks of 5 subjects, compute ave age and display the grade as per following rules:
# • average >= 90 : "A"
# • average >= 80 : "B"
# • average >= 70 : "C"
# • average >= 60 : "D"

subA=input("Marks of Subject 1 : ")
subB=input("Marks of Subject 2 : ")
subC=input("Marks of Subject 3 : ")
subD=input("Marks of Subject 4 : ")
subE=input("Marks of Subject 5 : ")
total=subA+subB+subC+subD+subE
avg=total/5
print("Total Marks : ",total)
print("Average : ",avg)
if avg>=90:
    print("Grade : A")
elif avg>=80:
    print("Grade : B")
elif avg>=70:
    print("Grade : C")
elif avg>=60:
    print("Grade : D")
