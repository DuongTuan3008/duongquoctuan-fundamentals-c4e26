song = {
    "CATENA": "Có ai thương em như anh",
    "ESRAXLED": "Em sai rồi anh xin lỗi em đi",
    "DML": "Duyên mình lỡ",
    "TCSTE": "Tất cả sẽ thay em",
    "NCL": "Như cái lò",
}
for k in song:
    print(k, end=" ")
print()
while True:
    i = input("Điền từ viết tắt: ")
    if i in song:   
        print(song[i])
        next_song = input("bạn có muốn tìm tiếp? (Y)")
        if next_song == "Y" or next_song == "y" or next_song == "":
            print()
        else: 
            print("Cảm ơn bạn!")
            break
    else: 
        choice = input("Không tìm được bài hát, bạn có muốn đóng góp bài này? (Y) ")
        if choice == "Y" or choice == "y" or choice == "":
            song[i] = input("Tên bài hát: ")
            print(song)
            next_song = input("bạn có muốn tìm tiếp? (Y)")
            if next_song == "Y" or next_song == "y" or next_song == "":
                print()
            else: 
                print("Cảm ơn bạn!")
                break
        else:
            next_song = input("bạn có muốn tìm tiếp? (Y)")
            if next_song == "Y" or next_song == "y" or next_song == "":
                print()
            else: 
                print("Cảm ơn bạn!")
                break
