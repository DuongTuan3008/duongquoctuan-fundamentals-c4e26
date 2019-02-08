while True:
    yob_str = input("Your year of birth? ")
    if yob_str.isdigit():
        yob = int(yob_str)
        if (1870 < yob < 2019):
            break 
    print ("You must enter a valid number, enter again!")
age = 2019 - yob
print(age)

    