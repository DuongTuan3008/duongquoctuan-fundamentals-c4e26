favs = ["pubg", "lol", "fortnite"]
print("Hi there, here you favorite things so far")
print("*"*50)
for n,i in enumerate(favs,1):
    print(n,i,sep=". ")
print("*"*50)
p = (input("favorite stuff you want to get rid of? ")) 
favs.remove(p)
print("*"*50)
for n,i in enumerate(favs,1):
    print(n,i,sep=". ")
print("*"*50)