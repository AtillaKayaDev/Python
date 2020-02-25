import requests
import html.parser
import json
from bs4 import BeautifulSoup

print("##### Meteo par villes au choix ##### \n")

city = input(str("Entrer le nom de la ville \n"))

def meteo(ville):
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + ville + '&appid=f38aa4800b84be81802294854cb750b6'
    HtmlContent = requests.get(url).text
    json1 = json.dumps(HtmlContent)
    print(json1)

meteo(city)