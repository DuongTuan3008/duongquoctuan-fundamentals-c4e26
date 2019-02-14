string=input("Enter a string: ")
lcase = string.lower()
words={}

for i in range(len(string)):
    if lcase[i]!=" ":
        words[lcase[i]]=lcase.count(lcase[i])
    else:
        i+=1
for (k,v) in sorted(words.items()):
    print(k,v)