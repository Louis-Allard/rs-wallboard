import requests
from bs4 import BeautifulSoup

url="https://www.instagram.com/l.allard/"

response=requests.get(url)
soup=BeautifulSoup(response.text, 'html.parser')

script=soup.findAll('script', {'type': 'text/javascript'})[3].text
print(script)