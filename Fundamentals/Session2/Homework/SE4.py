#4.a
print("* "*20)
#4.b
n = int(input("Enter a number: "))
print ("* "*n)
#4.c
print("x * "*4, end ="")
print("x")
#4.d
n = int(input("Enter a number: "))
if n%2 == 0: 
    m = int((n/2))
    print("x * "*m)
else:
    m = int((n-1)/2)
    print("x * "* m, end="")
    print("x")
#4.e
print()
#4.f
for i in range (1,4):
    print("* "*7)
    print()
#4.g
m = int(input("Enter n: "))
n = int(input("Enter m: "))
for i in range (1, m+1):
    print("* "*n)
    print()
