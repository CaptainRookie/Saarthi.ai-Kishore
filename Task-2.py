import re
password = input("Input your password : ")
check = True
while check:
    if (len(password) < 6 or len(password) > 12):
        break
    elif not re.search("[a-z]", password):
        break
    elif not re.search("[0-9]", password):
        break
    elif not re.search("[A-Z]", password):
        break
    elif not re.search("[!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]", password):
        break
    elif re.search("\s", password):
        break
    else:
        print("Valid Password")
        check = False
        break

if check:
    print("Not a Valid Password")
