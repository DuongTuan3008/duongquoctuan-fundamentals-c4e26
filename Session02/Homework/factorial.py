f = 1
n=int(input("Enter a number: "))
if n==0:
    print("The factorial of",n,"is 1")
else:
    for i in range(1,n+1):
        f *= i
print("The factorial of",n,"is",f)
