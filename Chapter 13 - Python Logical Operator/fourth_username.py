username = input("Enter Username : ")
if(username.isalpha()and (len(username)>5) and (type(username)!=None)):
    print("username is valid")
else:
    print("Usernamee is not valid")