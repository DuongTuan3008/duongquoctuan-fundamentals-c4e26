song = {
    "CATENA": "Có ai thương em như anh",
    "ESRAXLED": "Em sai rồi anh xin lỗi em đi",
    "DML": "Duyên mình lỡ",
    "TCSTE": "Tất cả sẽ thay em",
    "NCL": "Như cái lò",
}
i = input("Điền từ viết tắt: ")
if i in song:   
    print(song[i])
else: 
    print("Not found!")
