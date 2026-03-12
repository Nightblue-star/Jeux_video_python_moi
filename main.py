import sys
import time
from pymongo import MongoClient, DESCENDING
from utils import print_title

client = MongoClient('mongodb://localhost:27017/')
db = client['rpg_game']

def print_menu():
    print("1. Nouvelle Mission")
    print("2. Voir le Bingo Book")
    print("3. Quitter")

def lancer_option_choisi(choix):
    while True:
    #si option == 1
        if choix == "1":
            jeu()
            # jeu()
            #sinon si option == 2
        elif choix == "2":
            afficher_le_classement()
            #afficher_le_classement
            #sinon si option == 3
        elif choix == "3":
            print("\nSayonara !")
            sys.exit()
            # quitter_le_jeu

def afficher_le_classement():
    #afficher les top 3
    print_title("BINGO BOOK TOP 3 !")
    #

#verifier
def is_vallid (choix,min_val,max_val,):
    #verifier le choix est y a bien que lettre
    #si choix est un isdigit
    # alors verifier que choix c bien que des nombres
    if  choix.isdigit():
        choix_chiffre = int(choix)
        # est ce que il peut retourner rien
      #renvoi le  je sais pas         

        # si le choix est entre minval et maxval       
        if choix_chiffre >= min_val and choix_chiffre <= max_val :
            return True
            #cbon
            #sinon  
    return False
    #c cook
    
def recuperer_choix_valide(min_val,max_val):
    #tant que vrai 
    while True:
        #demander une saisi
        choix = input("\n Veillez saisir votre Choix: ")

        #si la saisie est valide
        if is_vallid(choix,min_val,max_val) :
            #renvoie saisie
            return choix
        #sinon
        else :
            print(f"Erreur votre choix doit etre comprix entre {min_val} et {max_val}")
            # afficher message d'erreur

def demander_nom_joueur():
    #tant que vrai
    while True : 
        #demander le prenom
        prenom = input("\nVotre nom de Ninja : ")
        #verfier si la chaine elle est pas vide
        # si le prenom est different du rien
        if prenom.strip() != "" :
            #on retourne prenom
            return prenom
        #sinon message d'erreur
        else :
            print("Erreur : Veillez écrire un nom de Ninja valide")


def afficher_perso_dispo(liste_heros):
    print("\n--- Ninjas Disponibles ---")
    for i,j in enumerate(liste_heros):
        print(f"{i+1}. {j['nom']} (ATK:{j['atk']} | DEF:{j['def']} | PV:{j['pv']})")



def creer_equipe(liste_heros):
    print_title("RECRUTEMENT")
    equipe = []

    while len(equipe) < 3:
        afficher_perso_dispo(liste_heros)
        choix = recuperer_choix_valide(1,len(liste_heros))
        hero_choisi = liste_heros[int(choix) - 1]
        equipe.append(hero_choisi)
        print(f"✅ {hero_choisi['nom']} recruté !")
        liste_heros.remove(hero_choisi)

    return equipe



def get_monstre_bdd() :
    monsters = [
        # Ennemis de base / Intermédiaires
        {"nom": "Zabuza Momochi",  "atk": 15, "def": 10, "pv": 80},
        {"nom": "Hidan",           "atk": 22, "def": 5,  "pv": 250}, #  PV énormes pour compenser le manque de technique
        {"nom": "Kakuzu",          "atk": 28, "def": 20, "pv": 180}, # 5 cœurs : Difficile à tuer
        {"nom": "Orochimaru",      "atk": 25, "def": 15, "pv": 150}, # Résistant et gluant
        {"nom": "Kisame Hoshigaki","atk": 28, "def": 20, "pv": 200}, # Le Bijuu sans queue (PV élevés)
        {"nom": "Deidara",         "atk": 30, "def": 5,  "pv": 110}, # Explosif mais fragile
        
        # Les Boss
        {"nom": "Pain (Tendô)",    "atk": 35, "def": 20, "pv": 220}, # Chef de l'Akatsuki
        {"nom": "Obito Uchiha",    "atk": 32, "def": 25, "pv": 200}, # Intouchable (Kamui)
        {"nom": "Madara Uchiha",   "atk": 40, "def": 30, "pv": 300}, # Légende ressuscitée
        {"nom": "Indra Otsutsuki", "atk": 45, "def": 35, "pv": 400}  # L'ancêtre (Boss Final)
    ]


def si_equipe_envie(liste_monstre):
    #retourner toute les personne en vie
    # on doit check chaque membre de la liste



def choisir_monstre_hasard():
    pass



def lancer_battle ():
    pass

def combattre(equipe):
    #creer le nombre de vague
    nb_vague = 0
    print("\n DEBUT DE LA GRANDE GUERRE NINJA ")
    while si_equipe_envie(equipe) :
        nb_vague += 1
        #importer les montres
        liste_monstres = get_monstre_bdd()
        monstre = choisir_monstre_hasard(liste_monstres)
        # cree la fonction battle qui fais la fonction combat
        lancer_battle(equipe, monstre)

        #si on gagne on soigne la team un peu
        if si_equipe_envie(equipe):
            print("L'equipe se soigne légèrement et avance ...")
    # on a perdu la mission
    print ("\n Mission Echouée : L'equipea été anéantie.")
    return nb_vague - 1

def sauvegarder_score():
    pass


def get_heros_bdd():
    
    heroes = [
        # Les classiques
        {"nom": "Naruto Uzumaki",  "atk": 30, "def": 20, "pv": 200}, # Kyubi = Beaucoup de PV
        {"nom": "Sasuke Uchiha",   "atk": 35, "def": 10, "pv": 140}, # Gros dégâts, un peu fragile
        {"nom": "Kakashi Hatake",  "atk": 28, "def": 12, "pv": 130}, # Équilibré
        {"nom": "Shikamaru Nara",  "atk": 20, "def": 18, "pv": 110}, # Stratège
        {"nom": "Rock Lee",        "atk": 32, "def": 5,  "pv": 120}, # Taijutsu pur : Attaque forte, Défense faible
        {"nom": "Gaara",           "atk": 24, "def": 25, "pv": 150}, # Défense absolue du sable
        {"nom": "Itachi Uchiha",   "atk": 34, "def": 8,  "pv": 110}, # Susanoo puissant mais maladie (PV faibles)
        
        # Les Nouveaux (Légendes)
        {"nom": "Minato Namikaze", "atk": 38, "def": 15, "pv": 160}, # L'éclair jaune : Très rapide et létal
        {"nom": "Shisui Uchiha",   "atk": 33, "def": 12, "pv": 130}, # Maître des illusions
        {"nom": "Hashirama Senju", "atk": 35, "def": 30, "pv": 220}  # Legende: Tank ultime (Bois + Régé)
    ]
    return heroes 




def jeu():
    #demander le prenom
    nom = demander_nom_joueur()
    # chercher la liste des heros en bdd
    liste_heros = get_heros_bdd()
    # Creer equipe
    equipe = creer_equipe(liste_heros)
    #Lancer le combat
    score = combattre(equipe)
    #Sauvegarder le score
    sauvegarder_score(score)

def main():
    while True:
        print_title("Naruto Shippuden RPG")
        print_menu()
        choix = recuperer_choix_valide(1,3)
        lancer_option_choisi(choix)




main()