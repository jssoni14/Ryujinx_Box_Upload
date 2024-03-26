import requests
from datetime import datetime
import json
import re
import sys
from bs4 import BeautifulSoup
from urllib import request
import os
data_ryu = "Ryujinx.zip"
path = "/Ryujinx/Ryujinx.zip"
ryujinx_with_date = ""
download_url = ""
Ryujinx_URL = []

current_datetime = datetime.now().strftime("%Y-%m-%d")
print("Current date: ", current_datetime)

str_current_datetime = str(current_datetime)
ryujinx_with_date = "Ryujinx_" + str_current_datetime + '.zip'


pattern_zip = "4.zip"
pattern_headless = "-ryujinx-"
url_links = []



urls = 'https://github.com/Ryujinx/release-channel-master/releases'
base_url = 'https://github.com'
grab = requests.get(urls)
soup = BeautifulSoup(grab.text, 'html.parser')


# traverse links from soup
for link in soup.find_all("a"):
   data = link.get('href')
   Ryujinx_URL.append(data)

for u in Ryujinx_URL:
   if re.search(pattern_zip, u):
    url_obj = re.search(pattern_headless, u)
    if not url_obj:
      url_obj_2 = re.search("archive", u)
      if not url_obj_2:
        download_url = u

download_url = base_url + download_url
print(download_url)
response = request.urlretrieve(download_url, ryujinx_with_date)