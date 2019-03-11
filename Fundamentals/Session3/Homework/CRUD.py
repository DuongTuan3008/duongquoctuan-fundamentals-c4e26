
our_items = ["T-shirt","Sweater"]
while True:
    Request = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    if Request =="R":
        print(our_items)
    elif Request =="C":
        new_item = input("Enter new item: ")
        our_items.append(new_item)
        print(our_items)
    elif Request == "U":
        updated_item = input ("Update position? ")
        if updated_item.isdigit() == True:
            new_item = input("New item? ")
            our_items.remove(our_items[int(updated_item)])
            our_items.insert(int(updated_item),new_item)
            print(our_items)
        else:
            print("Position is invalid. Please try again!")
    elif Request == "D":
        updated_item = input("Delete position? ")
        if updated_item.isdigit() == True:
            our_items.remove(our_items[int(updated_item)])
            print(our_items)
        else:
            print("Position is invalid. Please try again!")
    elif Request == "Exit":
        break
    else:
        Request = input("Cannot execute your request. Try again! ")