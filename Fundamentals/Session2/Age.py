cy = 2019 #current year
yob = input("What is birth year? ") #user_input_year
age = 2019 - int(yob)
print ("Your age is", age)
if age <10: # dieu kien
    print ("Baby")
elif age <18:
    print ("Teenager")
else:
    print('Adult')
print ("Bye bye")