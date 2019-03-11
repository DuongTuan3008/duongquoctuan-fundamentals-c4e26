favorite_list = ["footbal", "movie", "travel","coding", "cafe"]
print("Hi there, here your fav list so far:")
for i, x in enumerate(favorite_list,1):
    print(i, x, sep = ". ")
    
loop = True
while loop == True: 
    update_item = input("What you want to get rid of? ")
    if update_item.isdigit():
        update_item_num = int(update_item) -1
        if update_item_num > len(favorite_list) - 1:
            print("Position is invalid. Please try again")
        else:
            loop = False
            favorite_list.pop(update_item_num)
    else:
        if update_item == "":
            print("Value cannot be empty. Please try again")
        else:
            loop = False
            favorite_list.remove(update_item) 
    
for i, x in enumerate(favorite_list,1):
    print(i, x, sep = ". ")