import requests
from bs4 import BeautifulSoup

page = requests.get('https://jrescribe.com/transcripts/p1178.html')
soup = BeautifulSoup(page.text, 'html.parser')
content = soup.find(class_='content')

test = ''
for i in soup.find_all('div', 'content'):
    test = test + i.find('p').text

content.find_all('p')