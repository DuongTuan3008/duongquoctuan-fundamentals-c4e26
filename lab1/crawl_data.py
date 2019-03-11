#1. Creat connection
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url = "https://dantri.com.vn"
conn = urlopen(url)

#2. Download content
raw_data= conn.read()
page_content = raw_data.decode("utf8")

with open("dantri.html","wb") as f:
    f.write(raw_data)
# # print(page_content)

# #3. Find ROI
# soup = BeautifulSoup(page_content,"html.parser")
# # print(soup.prettify())
# ul = soup.find("ul","ul1 ulnew")

# #4. Extract ROI
# li_list = ul.find_all("li")
# new_list = []
# for li in li_list:
# # li= li_list[0]
#     h4= li.h4
#     a = h4.a
#     link =url + a["href"]
#     title = a.string
#     news = {
#         "link":link,
#         "title": title
#     }
#     new_list.append(news)
#     print(title)
#     print(link)
# pyexcel.save_as(records=new_list, dest_file_name="namth3.xlsx")
# print(h4)
# print(li)
# print(ul.prettify())






#5. Save 