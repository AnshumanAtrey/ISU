#Develop an application to check whether string is palindrome or not
x=input("Enter a string :")
def palindrome(y):
    for i in range(int(len(x)/2)):
        if y[i]!=y[len(y)-1-i]:
            return("Not Palindrome")
    return("Is Palindrome")
print(palindrome(x))