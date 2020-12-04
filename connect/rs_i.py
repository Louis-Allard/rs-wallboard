
import requests
from bs4 import BeautifulSoup

url="https://www.instagram.com/l.allard/"

response =  requests.get(url)
soup = BeautifulSoup(response, 'lxml').text
script = soup.findAll('script')[3]

print(script)