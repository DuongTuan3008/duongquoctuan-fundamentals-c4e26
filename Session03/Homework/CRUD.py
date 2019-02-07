items = ['T-Shirt', 'Sweater']
crud = input("Welcome to our shop, what do you want (C, R, U, D)? ")
if crud == 'R' or 'r':
    print(items)
elif crud == 'C' or 'c':
    items.append(input("Enter new item: "))
    print(items)
elif crud == 'U' or 'u':
    pos = int(input("Update position? "))
    items[pos-1] = input("New item? ")
    print(items)
elif crud == 'D' or 'd':
    pos = int(input("Delete position? "))
    del items[pos-1]
    print(items)
else:
    print("Please select one of the CRUD options!")