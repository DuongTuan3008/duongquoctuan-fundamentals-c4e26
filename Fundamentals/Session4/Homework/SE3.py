choice1 = {"1":35,"2":36,"3":40,"4":44}
choice2 = {"1": "About 55","2": "About 65","3": "About 75","4": "About 85"}
question1 = ["Answer following algebra question:","If x = 8, then what is the value of (4x + 3)? "]
question2 = ["Estimated this answer", "Jack score these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean?"]
Quiz = {"question": [question1, question2], "choice": [choice1, choice2],"answer":["4","2"] }
ur_answer_list = []
right_ans = 0 
for i in range(2):
    print(*Quiz["question"][i], sep = "\n")
    for k,v in Quiz["choice"][i].items():
        print(k,v,sep = ". ")
    ur_answer = input("Your choice: ")
    if ur_answer == Quiz["answer"][i]:
        print("Bingo")
    else:
        print(":(")
    ur_answer_list.append(ur_answer)
    if ur_answer_list[i] == Quiz["answer"][i]:
        right_ans =+1
print("You correctly answer",right_ans,"out of 2 questions.")
