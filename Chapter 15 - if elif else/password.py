password = ""
valid = False
if password:
    print("Password must not be empty")
    valid = False
if not len(password)>8:
    print("Password must be at least 8 characters")
if not (password == password.lower()):
    print("Password must contain at least 1 uppercase")
if not (password == password.upper()):
    print("Password must contain one lowercase")}