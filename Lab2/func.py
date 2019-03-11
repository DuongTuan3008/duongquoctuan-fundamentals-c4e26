# def sayhello(name):
#     print("Hello",name)
#call function
# list_name = ["Duc","Son", "Tuan"]
# for i in range(len(list_name)):
#     sayhello(list_name[i])
# for x in list_name:
#     name = x
#     sayhello()
# fruitful function with return
# def add(x,y):
#     a = x + y
#     return a
# add(3,4)

def calc(a,b,cal):
    result = None
    if cal == "+":
        result = a+b
    elif cal == "-":
        result = a-b
    elif cal == "*":
        result = a*b
    elif cal == "/":
        result = a/b
    return result