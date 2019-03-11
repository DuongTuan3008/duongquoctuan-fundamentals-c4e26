favorite_list = ["footbal", "movie", "travel"]
# new_favor = input("Tell me your favorite things: ")
# favorite_list.append (new_favor)
# print (*favorite_list, sep = ",")
Roman_num = ["I", "II", "III", "IV", "V"]
# for i in range (len(favorite_list)):
#     print(favorite_list[i].upper())
#     print(i+1, favorite_list[i].upper(), sep = ". ")
#     print(Roman_num[i], favorite_list[i].upper(), sep = ". ")
# for x in favorite_list:
#     print(x.upper())
# for i, x in enumerate(favorite_list):
#     print(i,x.upper(),sep=". ")
# for r, f in zip(Roman_num, favorite_list):
#     print(r, f)
print("Hi there, here your fav list so far:")
for i, x in enumerate(favorite_list,1):
    print(i, x, sep = ". ")
loop = True
while loop == True:
    update_item = input("Position you want to update? ")
    update_item_num = int(update_item) -1
    if update_item_num > len(favorite_list) - 1:
        print("Position is invalid. Please try again")
    else:
        loop = False
loop2 = True
while loop2 == True: 
    update_value = input ("Update value? ")
    if update_value == "":
        print("Value cannot be empty. Please try again")
    else:
        loop2 = False
     
    
favorite_list[update_item_num]= update_value

for i, x in enumerate(favorite_list,1):
    print(i, x, sep = ". ")