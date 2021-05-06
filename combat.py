# 2 classes : humain et robot
# Humain -> Plus de dégats si il fait des phrases longues
# Robot -> A le droit a une faute par phrase

# 5 type de mots -> sujet verbe complément liaison
# sujet -> peut etre en début de phrase, apres un verbe et apres une liaison -> peut finir une phrase si celle-ci contient un verbe
# verbe -> peut etre apres un sujet et apres une liaison -> peut finir une phrase
# complément -> peut etre apres un verbe -> peut finir une phrase
# liaison -> peut etre apres un sujet, un complément et un verbe -> ne peut pas finir une phrase

from os import system
import random

dictionnaire = {
    "ta mere" : "sujet",
    "ton pere" : "sujet",
    "ta soeur" : "sujet",
    "ton frere" : "sujet",
    "est moche" : "verbe",
    "et" : "liaison",
    "en string" : 'complement'
}

class Joueur:

    def __init__(self):
        self.nom = ''
        self.pv_max = 20
        self.pv = self.pv_max
        self.phrase = []
        self.phrase_finie = False
        self.classe = ''

    def Tour_joueur(self, tableau_mots):
        if self.phrase_finie != True:
            print("Que faites vous ? (choix d'un mot ou 'fin phrase')")
            choix = input("> ").lower
            if choix == "fin phrase":
                self.phrase_finie = True
            else :
                for mot in tableau_mots :
                    if choix == mot :
                        if check_phrase(self.phrase, choix):
                            tableau_mots.remove(choix)
                            self.phrase.append(choix)
                    else :
                        print("%s n'arrive pas a se décider et perd du temps" % self.nom)


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
    while tableau_mots.length < 10 :
        n_mot = random(0, len(dictionnaire))
        if not n_mot in tableau_mots :
            tableau_mots.append(dictionnaire[n_mot])  


def afficher_tableau(tableau_mots): #Affiche le tableau des mots utilisables
    system('cls')
    print(tableau_mots)


def calcul_degats(joueur1, joueur2): #Calcule et applique les dégats aux deux joueurs / si la fin de phrase n'est pas logique -1 dégats (ou 0?)
    degats_j1 = 0
    check_v = False
    for mots in joueur1.phrase:
        degats_j1 += 1
    if (joueur1.classe == 'humain' & degats_j1 >= 5): 
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
    while (joueur1.pv > 0 & joueur2.pv >0):
        afficher_tableau()
        while (len(tableau_mots) != 0 & joueur1.phrase_finie == False & joueur2.phrase_finie == False):
            joueur1.Tour_joueur(tableau_mots)
            joueur2.Tour_joueur(tableau_mots)
        calcul_degats(joueur1,joueur2)
        calcul_degats(joueur2,joueur1)
        joueur1.phrase = []
        joueur2.phrase = []