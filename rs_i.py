
import requests
from bs4 import BeautifulSoup
from instagramy import InstagramUser

user = InstagramUser('github')
user.biography
'''
print(user.is_verified)
print(user.number_of_followers)
print(user.number_of_posts)
'''

'''
url="https://www.instagram.com/l.allard/"

response =  requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
script = soup.findAll('script', {'type': 'text/javascript'})[3].text

print(script)
'''
