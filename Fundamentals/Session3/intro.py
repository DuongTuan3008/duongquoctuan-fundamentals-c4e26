# item1 = "Che"
# item2 = "Vit quay"
# item3 = "Trung vit lon"
# item4 = "Dau xot ca chua"

# items = [] #empty list
# print(items)
# print(type(items))

# items = ["Che"]
# print(items)

items = ["che", "chao long", "thit ga"]
# print(items)
# new_item = "trung vit lon"
# items.append (new_item)
# print(items)
#fori
# for i in range(len(items)):
#     print(items[i])
#foreach
# count = 1
# for x in items:
#     print(count, x, sep = ". ")
#     count +=1
# for i, x in enumerate (items,1):
#     print(i, x, sep = ". ")
#     print(items[1])
items.pop(1)
print(items)
items.remove("thit ga")
print(items)