#2.1
Sheep_sizes = [10,200,300,50,20,100]
count_months = 0
print("Hello, My name is Nam. These are my sheep sizes: ",Sheep_sizes)
while True:
    count_months = count_months + 1
#2.5
    if count_months > 4:
        break
#2.4
    for i in range (len(Sheep_sizes)):
        Sheep_sizes[i]=Sheep_sizes[i]+50*count_months
    print ("Month",count_months)
    print("After",count_months,"months, these are my sheep sizes: ",Sheep_sizes)
#2.2
    max_size = 0
    max_size_sheep = 0
    for i in range (len(Sheep_sizes)):
        if Sheep_sizes[i] >= max_size:
            max_size = Sheep_sizes[i]
            max_size_sheep = i
    print("The biggest size is",max_size,".Let shear it")
#2.3
    Sheep_sizes.remove(max_size)
    Sheep_sizes.insert(max_size_sheep,8)
    print("After shearing, these are my sheep sizes: ",Sheep_sizes)
    print()
#2.6
    Total_sheep_sizes= sum(Sheep_sizes)
    Money = 2 * Total_sheep_sizes
    print("My total Sheep sizes is: ",Total_sheep_sizes)
    print("I would get: ", Money)

  
    