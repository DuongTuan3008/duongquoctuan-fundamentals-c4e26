from random import *
def calc(a,b,cal):
    result = None
    if cal == "+":
        result = a+b
    elif cal == "-":
        result = a-b
    elif cal == "*":
        result = a*b
    elif cal == "/":
        result = int(round(a/b,0))
    return result
def generate_quiz():
    x= randint(0,20)
    y= randint(0,20)
    r= randint(-2,1)
    cal = choice(["+","-","*","/"])   
    z = calc(x,y,cal)+ r
    # print(" /x + /y = /z ")
    #string formating
    #s= f"{x} {cal} {y} = {z}"
    return x, y, cal, z

def check_answer(x, y, op, display_result, user_choice):
    ans = (calc(x,y,op) == display_result)
    if ans == user_choice:
        return True
    else:
        return False
