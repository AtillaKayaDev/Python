import requests
import html.parser
from bs4 import BeautifulSoup
import re

page = requests.get('https://www.data.gov', 'html.parser')
print(page)

soup = BeautifulSoup(page.text, "lxml") #Créer la soupe

StrNbDatasets = soup.h4.a.text.replace(',','') #Renvoi le texte se trouvant dans les balises h4,a, remplace les virgules par un vide
print(StrNbDatasets)

NbDatasets=int(re.search(r'\d+', StrNbDatasets).group()) #Transforme les chiffres contenus dans un string en int
print("il y'a", NbDatasets, "datasets disponibles")
