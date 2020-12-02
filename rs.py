from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


url = Request('https://twitter.com/lallard_59', headers={'User-Agent': 'Mozilla/5.0'})
response = urlopen(url).read()      
soup = BeautifulSoup(response, 'html.parser')

title = soup.find('span', class_= 'r-qvutc0')
    
print(title)  

