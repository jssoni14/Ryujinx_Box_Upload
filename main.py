import requests
import re
import sys
from bs4 import BeautifulSoup
from urllib import request

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
response = request.urlretrieve(download_url, "Ryujinx.zip")

