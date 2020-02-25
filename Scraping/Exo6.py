import requests
import html.parser
from bs4 import BeautifulSoup
import io
import re

print("Verification du nombre de followers twitter \n")
ident = input(str("Entrer le @ du compte à vérifier \n"))


def GetFollowersCount(id):
    url = 'https://twitter.com/'+id
    HtmlContent = requests.get(url).text
    soup = BeautifulSoup(HtmlContent, 'html.parser')
    # href="/NetflixFR/followers"
    NbAbo = soup.find('a', {'href' : "/" + id + "/followers"})['title']
    print(NbAbo)

    NbAboInt=int(re.search(r'\d+', NbAbo).group()) #Transforme les chiffres contenus dans un string en int
    print(NbAboInt)
    return NbAboInt


GetFollowersCount(ident)

