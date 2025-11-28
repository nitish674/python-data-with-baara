email = "test@gmail.com"
password = input("Enter Your Password : ")
valid = True
if not password:
    print("Password must not be empty")
    valid = False
if not len(password)>8:
    print("Password must be at least 8 characters")
    valid = False
if not any(c.islower() for c in password):
    print("Password must have at least 1 lowercase")
    valid = False
if not any(c.isupper() for c in password):
    print("Password must have at least 1 Uppercase")
    valid = False
if not(password!=email):
    print("Password must not be same as the email")
    valid = False
if not (password.count(" ")==0):
    print("Password must not contain any spaces")
    valid = False
if not (password[0].isalnum() and password[-1].isalnum()):
    print("password must start and end with a letter or digit")
    valid = False
if valid:
    print("Password is valid")

