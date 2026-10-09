"""Q14. Password Checker"""

username = input("Enter user name: ")
password = input("Enter password: ")

has_uppercase = False
has_lowercase = False
has_number = False
has_special = False

for ch in password:
    if ch >= "A" and ch <= "Z":
        has_uppercase = True
    elif ch >= "a" and ch <= "z":
        has_lowercase = True
    elif ch >= "0" and ch <= "9":
        has_number = True
    else:
        has_special = True

if username in password:
    print("Invalid Password")
else:
    print("Valid Password")

    if len(password) >= 8:
        if has_uppercase == True:
            if has_lowercase == True:
                if has_number == True:
                    if has_special == True:
                        print("Strong Password")
                    else:
                        print("Weak Password")
                else:
                    print("Weak Password")
            else:
                print("Weak Password")
        else:
            print("Weak Password")
    else:
        print("Weak Password")
