#1. create connection
from urllib.request import urlopen
from bs4 import BeautifulSoup
capital = input("Input your capital: ")
url = "https://wind.waqi.info/nsearch/full/{}?n=4".format(capital)
conn = urlopen(url)

#2. Download content
raw_data= conn.read()
page_content = raw_data.decode("utf8")


import json
page_content_dict = json.loads(page_content)   
time = page_content_dict['results'][0]['s']['t'][0]
AQI = page_content_dict['results'][0]['s']['a']
location = page_content_dict['results'][0]['s']['n'][0]

print("Date: ", time)
print("AQI: ", AQI)
print("Location: ", location)