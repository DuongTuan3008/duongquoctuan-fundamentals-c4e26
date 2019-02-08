from random import *
x = randint(0,100)
while True:
    n_str = (input("nhap so ma ban doan: "))
    if n_str.isdigit():
        n = int(n_str)
    if n < x:
        print("Too small :(")
    elif n > x:
        print("Too big :(")
    else:
        print("HOORAY!")
        break

    
