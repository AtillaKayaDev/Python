import requests
import html.parser
from bs4 import BeautifulSoup

page = requests.get('https://en.wikipedia.org/wiki/Main_Page', 'html.parser')
print(page)

soup = BeautifulSoup(page.text, "lxml") #Créer la soupe

for i in range (1,7):
    print(soup.find("h"+str(i)))

