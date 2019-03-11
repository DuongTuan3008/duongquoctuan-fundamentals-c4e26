print("Nhap vao hai so bat ky")
a = input("Nhap so thu nhat: ")
b = input("Nhap so thu hai: ")
# print("Tong hai so la: ", a+ b)
result = None
while True:
    cal = input("Phep toan: ")
    if cal == "+":
        result = int(a)+int(b)
        break
    elif cal == "-":
        result = int(a)-int(b)
        break
    elif cal == "*":
        result = int(a)*int(b)
        break
    else:
        print("Nhap phep toan khac")
print(result)
# Input ==> Process ==> Output Seperation of concern
