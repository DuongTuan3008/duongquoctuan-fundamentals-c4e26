import random
n = random.randint(1,100)
print (n)
u = 0
for i in range(1,n):
    if (n%i) ==0 :
        u = u+1
    else: 
        u = u
print (u)
 
if u == 1 :
    print ("n la so nguyen to")
else:
    print ("n ko phai la so nguyen to")
    