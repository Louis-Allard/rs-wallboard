
import requests
from bs4 import BeautifulSoup
import re
import json

url="https://www.instagram.com/l.allard/"

response =  requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
raw_script = soup.findAll('script')[4]
script = re.sub("<.*?>", "", str(raw_script))
clean = script.replace(";", "").replace("window._sharedData = ", "")

jsondata = json.loads(clean)
biography = jsondata["entry_data"]["ProfilePage"][0]["graphql"]["user"]
edge_followed_by = biography["edge_followed_by"]["count"]
edge_follow =  biography["edge_follow"]["count"]

print(edge_followed_by)
print(edge_follow)
