# 2 classes : humain et robot
# Humain -> Plus de dégats si il fait des phrases longues
# Robot -> A le droit a une faute par phrase

# 5 type de mots -> sujet verbe complément liaison
# sujet -> peut etre en début de phrase, apres un verbe et apres une liaison -> peut finir une phrase si celle-ci contient un verbe
# verbe -> peut etre apres un sujet et apres une liaison -> peut finir une phrase
# complément -> peut etre apres un verbe -> peut finir une phrase
# liaison -> peut etre apres un sujet, un complément et un verbe -> ne peut pas finir une phrase

from os import system
from random import *
import pygame 
import sys 

pygame.init() 
   
res = (1920,1080)  
screen = pygame.display.set_mode(res) 
   
color = (255,255,255) 
color_light = (170,170,170) 
color_dark = (100,100,100) 
  
width = screen.get_width() 
height = screen.get_height() 
  
#fond_combat = pygame.image.load('fond.jpg')
#screen.blit(fond_combat , (0, 0))

smallfont = pygame.font.SysFont('Corbel',35) 

def Texte(texte) :
    text = smallfont.render(texte , True , color) 
    return text

dictionnaire = {
    "ta mere" : "sujet",
    "ton pere" : "sujet",
    "ta soeur" : "sujet",
    "ton frere" : "sujet",
    "un chien" : "sujet",
    "un lama" : "sujet",
    "est moche" : "verbe",
    "pue" : "verbe",
    "suce" : "verbe",
    "mange" : "verbe",
    "et" : "liaison",
    "en string" : 'complement',
    "en slip" : 'complement',
}

class Joueur:

    def __init__(self):
        self.nom = ''
        self.pv_max = 20
        self.pv = self.pv_max
        self.phrase = []
        self.phrase_finie = False
        self.classe = ''
        self.etat = ''

    def Tour_joueur(self, tableau_mots):

        if self.phrase_finie != True:
        
            print(self.phrase) 
            mouse = pygame.mouse.get_pos()

            for ev in pygame.event.get():

                if ev.type == pygame.MOUSEBUTTONDOWN: 
                        
                    if 720 <= mouse[0] <= 720+480 and 180 <= mouse[1] <= 180+72: 
                        self.phrase.append(tableau_mots[0])
                        tableau_mots.remove(tableau_mots[0])
                        break
                    if 720 <= mouse[0] <= 720+480 and 252 <= mouse[1] <= 252+72: 
                        self.phrase.append(tableau_mots[1])
                        mot_choisi = True
                    if 720 <= mouse[0] <= 720+480 and 324 <= mouse[1] <= 324+72: 
                        self.phrase.append(tableau_mots[2])
                        mot_choisi = True
                    if 720 <= mouse[0] <= 720+480 and 396 <= mouse[1] <= 396+72:
                        self.phrase.append(tableau_mots[3])
                        mot_choisi = True
                    if 720 <= mouse[0] <= 720+480 and 468 <= mouse[1] <= 468+72: 
                        self.phrase.append(tableau_mots[4])
                        mot_choisi = True
                    if 720 <= mouse[0] <= 720+480 and 540 <= mouse[1] <= 540+72: 
                        self.phrase.append(tableau_mots[5])
                        mot_choisi = True
                    if 720 <= mouse[0] <= 720+480 and 612 <= mouse[1] <= 612+72: 
                        self.phrase.append(tableau_mots[6])
                        mot_choisi = True
                    if 720 <= mouse[0] <= 720+480 and 684 <= mouse[1] <= 684+72: 
                        self.phrase.append(tableau_mots[7])
                        mot_choisi = True
                    if 720 <= mouse[0] <= 720+480 and 756 <= mouse[1] <= 756+72: 
                        self.phrase.append(tableau_mots[8])
                        mot_choisi = True
                    if 720 <= mouse[0] <= 720+480 and 828 <= mouse[1] <= 828+72: 
                        self.phrase.append(tableau_mots[9])
                        mot_choisi = True
           

def check_phrase(phrase, mot): #Vérifie si le mot choisit est logique par rapport au mot précédent
    indice = len(phrase)
    if dictionnaire[mot] == "sujet" :
        if indice == 0 :
            return True
        else :
            if dictionnaire[phrase[indice-1]] == "sujet" :
                return False
            elif dictionnaire[phrase[indice-1]] == "verbe" :
                return True
            elif dictionnaire[phrase[indice-1]] == "complement" :
                return False
            elif dictionnaire[phrase[indice-1]] == "liaison" :
                return False
            else : print("le mot ne possede pas de type")

    if dictionnaire[mot] == "verbe" :
        if indice == 0 :
            return False
        else :
            if dictionnaire[phrase[indice-1]] == "sujet" :
                return True
            elif dictionnaire[phrase[indice-1]] == "verbe" :
                return False
            elif dictionnaire[phrase[indice-1]] == "complement" :
                return False
            elif dictionnaire[phrase[indice-1]] == "liaison" :
                return True
            else : print("le mot ne possede pas de type")

    if dictionnaire[mot] == "complement" :
        if indice == 0 :
            return False
        else :
            if dictionnaire[phrase[indice-1]] == "sujet" :
                return False
            elif dictionnaire[phrase[indice-1]] == "verbe" :
                return True
            elif dictionnaire[phrase[indice-1]] == "complement" :
                return False
            elif dictionnaire[phrase[indice-1]] == "liaison" :
                return True
            else : print("le mot ne possede pas de type")

    if dictionnaire[mot] == "liaison" :
        if indice == 0 :
            return False
        else :
            if dictionnaire[phrase[indice-1]] == "sujet" :
                return True
            elif dictionnaire[phrase[indice-1]] == "verbe" :
                return True
            elif dictionnaire[phrase[indice-1]] == "complement" :
                return True
            elif dictionnaire[phrase[indice-1]] == "liaison" :
                return False
            else : print("le mot ne possede pas de type")


def creer_tableau(): #Crée et retourne le tableau des mots utilisables en combat en évitant de mettre deux fois les memes mots
    i = 0
    tableau_mots = []
    dico = []
    for key, v in dictionnaire.items() :
        dico.append(key)
    while len(tableau_mots) < 10 :
        n_mot = randint(0, len(dico)-1)
        tableau_mots.append(dico[n_mot])  
    return tableau_mots

def afficher_tableau(tableau_mots):

    for i in range(10) :
        pygame.draw.rect(screen,color_dark,[720,180+72*i,480,72])
    for i in range(len(tableau_mots)) :
        screen.blit(Texte(tableau_mots[i]) , (720, 180+72*i)) #Mot 1
    pygame.display.update()

def calcul_degats(joueur1, joueur2): #Calcule et applique les dégats aux deux joueurs / si la fin de phrase n'est pas logique -1 dégats (ou 0?)
    degats_j1 = 0
    check_v = False
    for mots in joueur1.phrase:
        degats_j1 += 1
    if (joueur1.classe == 'humain' and degats_j1 >= 5): 
        degats_j1 += 2

    if dictionnaire[joueur1.phrase[len(joueur1.phrase)-1]] == "sujet" :
        for mot in joueur1.phrase :
            if dictionnaire[mot] == "verbe" :
                check_v = True
        if check_v == False :
            joueur2.pv -= degats_j1
        else :
            joueur2.pv -= degats_j1 - 1
    elif dictionnaire[joueur1.phrase[len(joueur1.phrase)-1]] == "verbe" :
        joueur2.pv -= degats_j1
    elif dictionnaire[joueur1.phrase[len(joueur1.phrase)-1]] == "complément" :
        joueur2.pv -= degats_j1
    else :
        joueur2.pv -= degats_j1 - 1


def combat(joueur1, joueur2):

    tableau_mots = creer_tableau()

    pygame.draw.rect(screen,color_dark,[81,64,240,60]) #Nom 1
    pygame.draw.rect(screen,color_dark,[81,180,472,835]) #Sprite 1

    pygame.draw.rect(screen,color_dark,[1599,64,240,60]) #Nom 2
    pygame.draw.rect(screen,color_dark,[1367,180,472,835]) #Sprite 2

    # #Tableau Mot
    # if 720 <= mouse[0] <= 720+480 and 180 <= mouse[1] <= 180+72: 
    #     pygame.draw.rect(screen,color_light,[720,180,480,72]) 
    # else : pygame.draw.rect(screen,color_dark,[720,180,480,72]) #Mot 1

    # if 720 <= mouse[0] <= 720+480 and 252 <= mouse[1] <= 252+72: 
    #     pygame.draw.rect(screen,color_light,[720,252,480,72]) 
    # else : pygame.draw.rect(screen,color_dark,[720,252,480,72]) #Mot 2

    # if 720 <= mouse[0] <= 720+480 and 324 <= mouse[1] <= 324+72: 
    #     pygame.draw.rect(screen,color_light,[720,324,480,72])     
    # else : pygame.draw.rect(screen,color_dark,[720,324,480,72]) #Mot 3

    # if 720 <= mouse[0] <= 720+480 and 396 <= mouse[1] <= 396+72: 
    #     pygame.draw.rect(screen,color_light,[720,396,480,72]) 
    # else : pygame.draw.rect(screen,color_dark,[720,396,480,72]) #Mot 4

    # if 720 <= mouse[0] <= 720+480 and 468 <= mouse[1] <= 468+72: 
    #     pygame.draw.rect(screen,color_light,[720,468,480,72]) 
    # else : pygame.draw.rect(screen,color_dark,[720,468,480,72]) #Mot 5

    # if 720 <= mouse[0] <= 720+480 and 540 <= mouse[1] <= 540+72: 
    #     pygame.draw.rect(screen,color_light,[720,540,480,72]) 
    # else : pygame.draw.rect(screen,color_dark,[720,540,480,72]) #Mot 6

    # if 720 <= mouse[0] <= 720+480 and 612 <= mouse[1] <= 612+72: 
    #     pygame.draw.rect(screen,color_light,[720,612,480,72]) 
    # else : pygame.draw.rect(screen,color_dark,[720,612,480,72]) #Mot 7

    # if 720 <= mouse[0] <= 720+480 and 684 <= mouse[1] <= 684+72: 
    #     pygame.draw.rect(screen,color_light,[720,684,480,72]) 
    # else : pygame.draw.rect(screen,color_dark,[720,684,480,72]) #Mot 8

    # if 720 <= mouse[0] <= 720+480 and 756 <= mouse[1] <= 756+72: 
    #     pygame.draw.rect(screen,color_light,[720,756,480,72]) 
    # else : pygame.draw.rect(screen,color_dark,[720,756,480,72]) #Mot 9

    # if 720 <= mouse[0] <= 720+480 and 828 <= mouse[1] <= 828+72: 
    #     pygame.draw.rect(screen,color_light,[720,828,480,72]) 
    # else : pygame.draw.rect(screen,color_dark,[720,828,480,72]) #Mot 10

    # if 840 <= mouse[0] <= 840+240 and 955 <= mouse[1] <= 955+60: 
    #     pygame.draw.rect(screen,color_light,[840,955,240,60]) 
    # else : 
    
    pygame.draw.rect(screen,color_dark,[840,955,240,60]) #Bouton finir phrase

    screen.blit(Texte("Nom 1") , (81, 64)) #Nom 1
    screen.blit(Texte("Nom 2") , (1599, 64)) #Nom 2
    screen.blit(Texte("Finir phrase"), (840, 955)) #Finir phrase

    while joueur1.pv > 0 and joueur2.pv >0 :
            while (len(tableau_mots) != 0 and (joueur1.phrase_finie == False and joueur2.phrase_finie == False)):
            
                afficher_tableau(tableau_mots)
                joueur1.Tour_joueur(tableau_mots)
                afficher_tableau(tableau_mots)
                joueur2.Tour_joueur(tableau_mots)    

            calcul_degats(joueur1,joueur2)
            calcul_degats(joueur2,joueur1)
            tableau_mots = creer_tableau()

            joueur1.phrase = []
            joueur2.phrase = []

J1 = Joueur()
J1.classe = 'humain'
J1.etat = 'combat'
J2 = Joueur()

mouse = pygame.mouse.get_pos() 
         
combat(J1,J2)
