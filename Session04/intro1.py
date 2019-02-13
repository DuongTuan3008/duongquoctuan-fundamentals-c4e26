# person = ["H.Duc", 24, "Hai Phong", 11, False, 430, True]

# person = {}
# print(person)
# print(type(person))

# person = {
#     "name": "H.Duc"
# }
# print(person)

person = {
    "name": "H.Duc",
    "age": 24,
    "Location": "Hai Phong",
    "status": False,
}
print(person)
k = input("Enter code: ")
if k in person:
    print(person[k])
else: 
    print("Not found")
