while True:
    yob_string = input("What is birth year? ") #user_input_year
    if yob_string.isdigit():
        yob = int(yob_string)
        if yob < 2019:
            break
        else:
            print("You must enter a valid number")
    else:
        print("You must enter a number!")

age = 2019 - yob
print ("Your age is", age)