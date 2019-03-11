answer = {"1":35,
"2":36,
"3":40,
"4":44}
loop = True
while loop == True: 
    print("Answer following algebra question:")
    print("If x = 8, then what is the value of (4x + 3)? ")
    for k, v in answer.items():
        print(k, v, sep = ". ")
    ur_answer = input("Your choice: ")
    if ur_answer == "4":
        print("Bingo")
        loop = False
    else:
        print(":(")