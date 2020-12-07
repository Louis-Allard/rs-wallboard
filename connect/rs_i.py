
import requests
from bs4 import BeautifulSoup
import re

url="https://www.instagram.com/l.allard/"

response =  requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
raw_script = soup.findAll('script')[3]

script = re.sub("</script>"," ",raw_script.text)

print(script)