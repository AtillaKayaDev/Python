import requests
import html.parser
from bs4 import BeautifulSoup

page = requests.get('https://fr.wikipedia.org/wiki/%C3%89lisabeth_II', 'html.parser')
print(page)

soup = BeautifulSoup(page.text, "lxml")

images = soup.find('div',id='bodyContent')
img1 = images.findAll('img')
#img = img1.findAll('src')

for elem in img1:
    link = elem.get('src')
    print(link)