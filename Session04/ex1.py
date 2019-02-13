favs = ["pubg", "lol", "fortnite"]
print("Hi there, here you favorite things so far")
print("*"*50)
for n,i in enumerate(favs,1):
    print(n,i,sep=". ")
print("*"*50)
p = (input("Position you want to update? "))
while True:
    while p.isdigit():
        p_int = int(p)
        favs[p]= input("Enter your new favorite: ")
        for n,i in enumerate(favs,1):
            print(n,i,sep=". ")
            print("*"*50)
        break
    else: 
        print("Enter a number!")
        p = (input("Position you want to update? "))

