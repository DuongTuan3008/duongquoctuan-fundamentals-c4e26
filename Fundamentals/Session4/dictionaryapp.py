Capital = {"VietNam":"Hanoi",
"Indonesia":"Jakarta",
"Malaysia":"Kualalumpur",
"Japan":"Tokyo",
"China":"Beijing",
"Korean":"Seoul"}
for key in Capital:
    print(key)
loop = True
while loop == True: 
    Country = input("Enter your country: ")
    if Country in Capital:
        print(Capital[Country])
    elif Country == "Exit":
        loop = False
    else: 
        update_request = input("The country is not in our list. Do you want to update (Y/N)? ")
        if update_request == "Y":
            Capital_new = input("Enter a capital: ")
            Capital[Country] = Capital_new
            for key in Capital:
                print(key)
        else:
            for key in Capital:
                print(key)
