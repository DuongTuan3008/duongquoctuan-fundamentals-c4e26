favs = ["pubg", "lol", "fortnite"]
print("Hi there, here you favorite things so far")
print("*"*50)
for n,i in enumerate(favs,1):
    print(n,i,sep=". ")
print("*"*50)
p = int(input("Position you want to get rid of? ")) -1
favs.pop(p)
print("*"*50)
for n,i in enumerate(favs,1):
    print(n,i,sep=". ")
print("*"*50)