# person = ["H.Duc", 24, "Hanoi",11, False, 43, True]

# person = {}
# print(person)
# print (type(person))

p0 = {
    "name" : "H.Duc", # key : value , type(key) = string 
    "age" : 24,
    "Hometown": "HaiPhong",
    "Status" : False,
    "Friend" : 43,
    "Available": True,
    "favs":["book","movie","music"] 
}
p1 = {
    "name" : "Hoang", # key : value , type(key) = string 
    "age" : 21,
    "Hometown": "Hanoi",
    "Status" : False,
    "Friend" : 43,
    "Available": True,
    "favs":["book","movie","music"] 
}
p2 = {"name" : "Quang", # key : value , type(key) = string 
    "age" : 24,
    "Hometown": "Ha Nam",
    "Status" : False,
    "Friend" : 25,
    "Available": True,
    "favs":["book","movie","music"] 
}
p3 = {
    "name" : "Son", # key : value , type(key) = string 
    "age" : 21,
    "Hometown": "Hung Yen",
    "Status" : False,
    "Friend" : 56,
    "Available": True,
    "favs":["Cafe","Coding"] 
}
# print(person["Hometown"]),
# person["friend_count"]=450
# person["age"] +=2
# print (person)
# for k in person:
#     print(k,person[k])
# for v in person.values():
#     print(v)
# for k,v in person.items():
#     print(k,v)
# print(person.items())
# fs = person["favs"]
# print(person["favs"][1])
p_list =[]
# p_list.append(p0)
# p_list.append(p1)
# p_list.append(p2)
# p_list.append(p3)
p_list= [
{
    "name" : "H.Duc", # key : value , type(key) = string 
    "age" : 24,
    "Hometown": "HaiPhong",
    "Status" : False,
    "Friend" : 43,
    "Available": True,
    "favs":["book","movie","music"] 
},
p1,
p2,
p3]
print(p3["favs"][0])
