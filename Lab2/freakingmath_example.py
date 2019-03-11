from random import randint, choice

from func import calc

x= randint(1,20)
y= randint(1,20)
r= randint(-2,1)
cal = choice(["+","-","*","/"])   
z= calc(x,y,cal)+r
# print(" /x + /y = /z ")
#string formating
s= f"{x} {cal} {y} = {z}"
print(s)
ans = input("Y/N? ")
a = (calc(x,y,cal) == z)
b = (ans == "Y")
if a == b:
    print("yay")
else:
    print("wrong")

