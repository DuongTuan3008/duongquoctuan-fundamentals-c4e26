from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)

raw_data= conn.read()
page_content = raw_data.decode("utf8")
with open("cafef.html","wb") as f:
    f.write(raw_data)


soup = BeautifulSoup(page_content,"html.parser")
table_data = soup.find("table",id={"tableContent"})

tr_list = table_data.find_all('tr')
new_list = []
for tr in tr_list:
    cols=tr.find_all('td')
    for x in cols:
        cols = x.text.strip()
        if not len(cols)<3:
            new_list.append({cols[0]:cols[1:]})
        
        
pyexcel.save_as(records=new_list, dest_file_name="cafef.xlsx")
