from ex1 import db

collection=db["posts"]
new_collection = {
    "title":"ANH CÓ ƯỚC GÌ ĐÂU",
    "author":"Dương Quốc Tuấn",
    "content":"""
Anh có ước gì đâu
Một ngôi nhà
Bão dừng sau cánh cửa
Những ưu tư muộn phiền tạm thời bỏ lại
Bên trong, chỉ có ấm áp, và em
Anh có ước gì đâu: Một tách cà phê
Một buổi sáng yên lành
Ta tất bật đón chào ngày mới
Hôm qua là điều đã lùi xa.
Những điều to tát như yêu thương, hờn giận, thứ tha
Hãy để dành cho chú chim đang hót bên ngoài cửa sổ
Đang chờ em là rau đầy một rổ
Bó hoa đang chờ cắm
Và một ngày bận rộn
Của anh.
Anh già rồi
Nên sẽ không thích kiêng khem
Ăn uống ngon, mặc đẹp, đọc những quyển sách hay
Đi lang thang đó đây
Vùi đầu vào việc làm
Hát khi tắm, xem phim khi đang nằm, cuộn tròn khi ngủ
Và yêu em khi anh muốn.
Anh có ước gì đâu
Em ạ!
Cuộc đời này, là phức hợp của những điều giản dị
Ta cứ sống, thở, cầu nguyện và yêu thôi!
Mọi thứ, hoặc chỉ là bản thân nó
Hoặc vốn dĩ đã là một phép màu."""
 }
collection.insert_one(new_collection)

