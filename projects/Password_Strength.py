import string

password = input("Enter password: ")
password_len = len(password)

hasUpper = False
hasLower = False
hasDigit = False
hasPunctuation = False

for c in password:
    if c.isupper():
        hasUpper = True
    if c.islower():
        hasLower = True
    if c.isdigit():
        hasDigit = True
    if c in string.punctuation:
        hasPunctuation = True

if password_len >= 8 and hasUpper and hasLower and hasDigit and hasPunctuation:
    print("Password meets all requirements.")
else:
    if password_len < 8:
        print("Password needs at least 8 characters.")
    if not hasUpper:
        print("Password needs at least 1 uppercase letter.")
    if not hasLower:
        print(" Password needs at least 1 lowercase letter.")
    if not hasDigit:
        print("Password needs at least 1 digit.")
    if not hasPunctuation:
        print("Password needs at least 1 special character.")
