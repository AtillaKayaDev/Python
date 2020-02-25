import requests
import html.parser
from bs4 import BeautifulSoup

page = requests.get('https://www.data.gov', 'html.parser')
print(page)

soup = BeautifulSoup(page.text, "lxml") #Créer la soupe

head = soup.h1 #Attribue H1 à head
print(head.contents) #retourne le contenu de la balise H1


