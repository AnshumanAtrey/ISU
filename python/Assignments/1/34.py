input_string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count=0
for i in input_string:
    if i in vowels:
        count+=1
print("Number of vowels:", count)

