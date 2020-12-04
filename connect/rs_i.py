
import requests
from bs4 import BeautifulSoup

url="https://www.instagram.com/l.allard/"

response =  requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
script = soup.findAll('span')

print(script)





