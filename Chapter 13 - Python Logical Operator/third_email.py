email = input("Enter Email : ")
if(email and ("@" in email) and email.endswith(".com")):
   print("Email is Valid")
else:
    print("Email is not valid")