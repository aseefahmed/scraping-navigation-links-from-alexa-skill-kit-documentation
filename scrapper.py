import requests
from bs4 import BeautifulSoup
import pandas as pd

data = pd.DataFrame()
endpoint = "https://developer.amazon.com/en-US/docs/alexa/ask-overviews/build-skills-with-the-alexa-skills-kit.html"
response = requests.get(endpoint)

soup = BeautifulSoup(response.text, "lxml")
lis = soup.find_all('li', {"class": ["level1", "level2", "level3", "level1items", "level2items", "level3items"]})

paths = []
texts = []
base_uri  = "https://developer.amazon.com/en-US/docs/alexa/"
for li in lis:
    path = li.find('a').get('href')
    text = li.find('a').text
    if(path == "#"):
        url = ""
    else:
        url = base_uri + path[2:]
    paths.append(url)
    texts.append(text)
    
data['Topic'] = texts
data['Link'] = paths

data.to_excel('alexa_navigation_links.xlsx', index=False)
