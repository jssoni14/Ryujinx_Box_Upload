import requests
from datetime import datetime
import json
import re
import sys
from bs4 import BeautifulSoup
from urllib import request
import dropbox
import os
data_ryu = "Ryujinx.zip"
path = "/Ryujinx/Ryujinx.zip"
ryujinx_with_date = ""

DROPBOX_API_KEY = os.environ["DROP_BOX_KEY"]
print(DROPBOX_API_KEY)
dbx = dropbox.Dropbox(DROPBOX_API_KEY)
dbx.users_get_current_account()

current_datetime = datetime.now().strftime("%Y-%m-%d")
print("Current date: ", current_datetime)

str_current_datetime = str(current_datetime)
ryujinx_with_date = "Ryujinx_" + str_current_datetime + '.zip'

url = "https://content.dropboxapi.com/2/files/upload"
pattern_zip = "4.zip"
url_links = []



urls = 'https://github.com/Ryujinx/release-channel-master/releases'
base_url = 'https://github.com'
grab = requests.get(urls)
soup = BeautifulSoup(grab.text, 'html.parser')

# opening a file in write mode
f = open("Ryzu_links.txt", "w")
# traverse paragraphs from soup
for link in soup.find_all("a"):
   data = link.get('href')
   f.write(data)
   f.write("\n")

f.close()
with open("test1.txt", "r") as text_file:
  for line in text_file:
      if re.search(pattern_zip, line):
          print(line)
          url_links.append(line)


download_url = base_url + url_links[0]
print(download_url)
response = request.urlretrieve(download_url, ryujinx_with_date)
for entry in dbx.files_list_folder('').entries:
    print(entry.name)
ryujinx_path_dbx = '/Ryujinx/'+ ryujinx_with_date
with open(data_ryu, "rb") as f:
    res = dbx.files_upload(f.read(), ryujinx_path_dbx, mute = True)
    print(res)
#dbx.files_upload(data.read(), path)
#data = open("Ryujinx.zip", "rb").read()

#r = requests.post(url, headers=headers, data=data)
#print(r)