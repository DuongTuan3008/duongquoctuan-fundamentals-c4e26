import random
WORDS = ("handkerchief","cemetery","conscience",
"playwright","rhythm","pabulum",
"pabulum","intransigent")

print(
"""
    Chào mừng đến với trò chơi của Tuấn!

Đảo vị trí của các chữ cái để tạo thành một từ (Tiếng Anh)
        (Nhấn phím Enter để thoát)
"""
)


play=input("Bạn có muốn chơi không? (có hoặc không) ")
while play=="có":
    word = random.choice(WORDS)
    correct = word
    jumble =""
    while word:
        position = random.randrange(len(word))
        jumble += word[position] +" "
        word = word[:position] + word[(position + 1):]

    print("Câu hỏi là:", jumble)
    points=100
    guess = input("\nCâu trả lời của bạn: ")
    while guess != correct and guess != "":
        print("Rất tiếc, câu trả lời không chính xác.")
        guess = input("Câu trả lời của bạn: ")

    if guess == correct:
        print("Hura, Câu trả lời chính xác!\n")
        print("Điểm của bạn: "+str(points))
        play=input("Bạn có muốn chơi tiếp? (có hoặc không) ")
    elif guess== "":
        print("Bạn đã thất bại...")
        play=input("Bạn có muốn chơi lại? (có or không) ")


print("Thanks for playing.")

input("\n\nNhấn phím ENTER để thoát.")