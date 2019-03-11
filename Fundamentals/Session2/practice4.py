import getpass
print("Welcom to super user gateway")
username = getpass.getpass("Username = ")
if username != "c4e":
    print("You are not super user")
else: 
    password = input ("Password = ")
    if password == "codethechange":
        print("Welcome super user")
    else:
        print("Password incorrect")
    
    