Things_I_like = ["Game","cafe",]
print(*Things_I_like, sep=", ")
Things_I_like.append(input("Name one thing to add: "))
print(*Things_I_like, sep=", ")