import sys
import time
from pymongo import MongoClient, DESCENDING
from models import Hero
from game import start_combat
# On importe nos nouvelles fonctions utilitaires
from utils import print_title, display_team_summary, clear_screen

# Connexion DB
client = MongoClient('mongodb://localhost:27017/')
db = client['rpg_game']

def show_leaderboard():
    """Affiche les meilleurs scores."""
    print_title("BINGO BOOK (TOP 3)")
    scores = list(db.scores.find().sort("vagues", DESCENDING).limit(3))
    
    if not scores:
        print("   Aucun record pour l'instant.")
    else:
        for i, s in enumerate(scores):
            print(f"   {i+1}. {s['username']} - {s['vagues']} vagues")
    input("\nAppuyez sur Entrée pour revenir...")

def create_team():
    """Gère la création de l'équipe avec affichage propre."""
    available = list(db.heroes.find())
    my_team = []
    
    while len(my_team) < 3:
        clear_screen()
        print_title("RECRUTEMENT")
        
        # On utilise utils.py pour afficher l'équipe en cours
        display_team_summary(my_team)
        
        print("\n--- Ninjas Disponibles ---")
        for i, h in enumerate(available):
            print(f"{i+1}. {h['nom']} (ATK:{h['atk']} | DEF:{h['def']} | PV:{h['pv']})")
            
        try:
            choice = input("\n👉 Choisissez un numéro : ")
            idx = int(choice) - 1
            if 0 <= idx < len(available):
                selected = available.pop(idx)
                my_team.append(Hero(selected))
                print(f"✅ {selected['nom']} recruté !")
                time.sleep(1)
            else:
                print("❌ Numéro invalide.")
                time.sleep(1)
        except ValueError:
            print("❌ Entrez un chiffre.")
            time.sleep(1)
            
    return my_team

def main():
    while True:
        clear_screen()
        print_title("NARUTO SHIPPUDEN RPG")
        print("1. Nouvelle Mission")
        print("2. Voir le Bingo Book")
        print("3. Quitter")
        
        choice = input("\nChoix : ")
        
        if choice == "1":
            username = input("\nVotre nom de Ninja : ") or "Anonyme"
            team = create_team()
            
            # Lancement du combat
            score = start_combat(team, db)
            
            # Sauvegarde
            db.scores.insert_one({"username": username, "vagues": score})
            print_title(f"FIN DE PARTIE - Score : {score}")
            time.sleep(3)
            
        elif choice == "2":
            show_leaderboard()
            
        elif choice == "3":
            print("\nSayonara !")
            sys.exit()

if __name__ == "__main__":
    main()