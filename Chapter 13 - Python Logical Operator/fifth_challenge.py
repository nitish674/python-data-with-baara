is_admin = False
is_moderator = True
is_banned = False
is_mailverified = True

if((is_admin or is_moderator)and (not is_banned) and is_mailverified):
    print("User is Valid")
else:
    print("User is not valid")