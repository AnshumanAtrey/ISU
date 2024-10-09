count=0
while count<3:
    user,pwd=input("Enter Username & Password").split
    if user=="admin" and pwd=="pass":
        print("Login Successful")
        break
    else:
        if count==2:
            print("Sorry attempt complete")
        else:
            print("Login Failed")
        count+=1

