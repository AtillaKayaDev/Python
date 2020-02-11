########## Version simplifiée du Black Jack ##########

import random 
import math
import os
import sys

#Création du jeu de carte
#Créer un dictionnaire contenant la couleur et le numero de la carte comme key, et sa valeur comme value
def CreerJeuCartes():

    JeuCartes={}

    Couleur=["Coeur","Carreau","Trèfle","Pique"]
    Num=["As ","2 ","3 ","4 ","5 ","6 ","7 ","8 ","9 ","10 ","Valet ","Dame ","Roi "]
    Valeur=[10,2,3,4,5,6,7,8,9,10,10,10,10]

    for i in Couleur:
        for j,k in zip(Num,Valeur):
            JeuCartes[j+i]=k

    return JeuCartes

#Créer une main de deux cartes pour le joueur et pour le dealer
def CreerMain():

    i=0
    CJC=CreerJeuCartes()
    MainJ={}
    MainD={}

    while i < 2: #Attribue une carte tirée au hasard du jeu au joueur, puis au dealer, puis se répète une fois

        a=random.choice(list(CJC.items()))
        dic={a[0] : a[1]}
        MainJ.update(dic)
        CJC.pop(a[0])
    
        b=random.choice(list(CJC.items()))
        dic={b[0] : b[1]}
        MainD.update(dic)
        CJC.pop(b[0])
        
        i=i+1

    return MainJ,MainD

CM=CreerMain()

#Calcul la somme des valeurs des cartes tirés pour le joueur et le dealer, retourne leur nombres de points   
def CalculPoints(M1,M2):

    PointsJ=0
    PointsD=0

    PointsJ=sum(M1.values())
    PointsD=sum(M2.values())

    return PointsJ,PointsD

# Attribue une carte tirée au hasard du jeu au joueur puis retourne sa main réactualisée
def TirerCarte(Main,Jeu): 

    a=random.choice(list(Jeu.items()))
    dic={a[0] : a[1]}
    Main.update(dic)
    Jeu.pop(a[0])
    
    return dic, Main
    
#Affiche la main du joueur et du dealer ainsi que leurs points
def Totaux(M1,PT,pers):

    main=M1
    pts=PT
    print("Main",pers, ":" , main ,"\n ", pts , " points")

#Affiche un message selon l'état du jeu (black jack, 21 points etc...)
def Message(ptsJ,ptsD):

    msj = str
        
    if ptsJ > ptsD:       
        if ptsJ < 22:
            if ptsJ == 21:
                if len(CM[0])==2:
                    msj="Bravo ! Black Jack $$$"
                else:
                    msj="Bravo ! Tu as 21 points"
            else:
                msj="Tu as gagné !"
        else:
            msj="Perdu ! Tu as depassé les 21 points"
    
    if ptsD > ptsJ: 
        if ptsD <22:
            msj="Perdu ! Le croupier est plus proche des 21 points"
        else:
            msj="Bravo ! Le croupier a depassé 21"
    if ptsD==ptsJ:
        msj="Egalité"
    
    print(msj)

#Demande au joueur s'il veux relancer une partie
def relance(): 

    q = input("\n Voulez vous relancer une partie ? [y/n] > ")

    if q == "y":
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 
    else:
        print("\n Fermeture du programme...")
        sys.exit(0)

#Simule le jeu
def PlayGame():
    
    CJC=CreerJeuCartes()
    CM=CreerMain()
    
    Totaux
    quest=str
    
    print("\nBienvenue a la version simplifiée du Black Jack !  \n")
    quest=str(input("Voulez vous lancer une partie ? [y/n] \n"))

    if quest=="y":
        
        print("Voici votre main : \n", CM[0])
        print("Voici celle du dealer : \n", CM[1])
        CP=CalculPoints(CM[0],CM[1])
        print("\nVous avez",CP[0]," points \n")
        print("Le dealer a ", CP[1]," points \n")
        
 
    while input("Voulez vous tirer une carte ? [y/n]") == "y":
        TC=TirerCarte(CM[0],CJC)
        print("\nVoici la carte tirée :", TC[0] ,"\n")
        print("Voici votre main :", TC[1] , "\n")
        CP=CalculPoints(CM[0],CM[1])
        print("Voici votre nombre de points :", CP[0])
    
    
    CP=CalculPoints(CM[0],CM[1])
    
    while CP[1]<= 17:

        TirerCarte(CM[1],CJC)
        print("Voici la nouvelle main du dealer", CM[1])
        CP=CalculPoints(CM[0],CM[1]) 
        print("Le dealer a desormais :", CP[1], " points")

    Totaux(CM[0],CP[0],"Joueur")
    Totaux(CM[1],CP[1],"Dealer")
    
    Message(CP[0],CP[1])
   
PlayGame()
relance()














