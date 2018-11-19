import requests
from bs4 import BeautifulSoup

url = "https://www.ranwena.com/files/article/84/84953/"
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
i = 0
for list in soup.select('#list'):
    while i < len(soup.select('dd')):
        name = list.select('dd')[i].text
        href = list.select('a')[i]['href']
        i = i + 1
        print(name,href)
print(i)
