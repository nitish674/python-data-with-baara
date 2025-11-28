password = input("Enter Your Password :")
if(len(password)>=8 and not " "in password):
    print("password is valid")
else:
    print("password is not valid")