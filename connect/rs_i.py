
import requests
from bs4 import BeautifulSoup
import re

url="https://www.instagram.com/l.allard/"

response =  requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
raw_script = soup.findAll('script')[4]
script = re.sub("<.*?>", "", str(raw_script))
clean = script.replace(";", "").replace("window._sharedData = ", "")

print(clean)