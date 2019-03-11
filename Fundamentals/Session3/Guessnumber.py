import random
n  = random.randint(1,100)
count = 0
while True: 
    count += 1
    number_string = input("Guess my number: ")
    x = int(number_string)
    
    if x < n:
        print("Try again. My number is bigger than that")
    elif x > n: 
        print("Try again. My number is smaller than that")
    else: 
        print("Bingo")
        break
    if count > 7:
        print("Oops. Game is over")
        break