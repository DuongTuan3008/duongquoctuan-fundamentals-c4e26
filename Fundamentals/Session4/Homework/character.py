words = input ("Enter a word: ")
words_lower = words.lower()
words_list = {}
for i in range(len(words)):
    if words[i]==" ":
        print()
    else:
        words_list[words_lower[i]]= words_lower.count(words_lower[i]) 
for k,v in sorted(words_list.items()):
    print(k,v)