email = "-reeshu@gmail.com"
# Clean Email First
email = email.strip()
# Email must be not empty
if email == "":
    print("Email Cannot be empty")
elif not ('.' in email and '@' in email):
    print("Email Must Contain . and @")
elif not email.count('@')==1:
    print("Email Must contain exactly 1 @")
elif not (email.endswith(('.com','.net','.org'))):
    print("Email must contain .com,.org,.net")
elif not (len(email)<254):
    print("Email must Contain more than 254 characters")
elif not (email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with a letter or number")         
else:
    print("Email is valid")