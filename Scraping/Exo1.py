import requests 

page = requests.get('https://fr.wikipedia.org/robots.txt')

print(page) #Renvoi réponse, accessible ou non (200 / 403 / etc...)

print(page.text) #Renvoi le contenu du lien

print(page.content) #Renvoi contenu HTML