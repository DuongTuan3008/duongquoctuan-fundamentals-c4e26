print("Hello, my name is Tuấn and these are my sheep sizes")
sheep = [5,7,300,90,24,50,75]
print(sheep)
print()
sum = 0
for m in range(3):
    print("MONTH",m+1)
    print("Now my biggest sheep has size",max(sheep),"let's shear it")
    sheep[sheep.index(max(sheep))] = 8
    print("After shearing, here's my flock")
    print(sheep) 
    print("One month has passed, now here is my flock")
    sheep1=[]
    for i in sheep:
        i += 50
        sheep1.append(i)       
    print(sheep1)
    sheep = sheep1
    print()
for i in sheep:
    sum += i
print("My flock has size in total: ",sum,"\nI would get ",sum,"*2$ = ",sum*2,sep='')
