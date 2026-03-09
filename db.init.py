from pymongo import MongoClient

# ==========================================
# 1. CONFIGURATION ET CONNEXION
# ==========================================
# On se connecte au client MongoDB hébergé dans Docker.
# 'localhost' fonctionne car le port 27017 du conteneur est redirigé vers ta machine.
client = MongoClient('mongodb://localhost:27017/')

# On sélectionne (ou crée) la base de données nommée 'rpg_game'.
db = client['rpg_game']

def init_db():
    print("--- Démarrage de l'initialisation ---")

    # ==========================================
    # 2. NETTOYAGE (RESET)
    # ==========================================
    # On vide les collections 'heroes' et 'monsters' avant de les remplir.
    # Cela évite d'avoir des doublons (ex: 50 Naruto) si on lance le script plusieurs fois.
    db.heroes.delete_many({})
    db.monsters.delete_many({})
    print(" Base de données nettoyée : Anciennes données supprimées.")
    
    # ==========================================
    # 3. CRÉATION DES HÉROS (TEAM KONOHA)
    # ==========================================
    # Chaque héros a des stats basées sur le Lore de Naruto :
    # - ATK : Dégâts infligés
    # - DEF : Dégâts réduits quand on se fait taper
    # - PV  : Points de vie
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
    
    # ==========================================
    # 4. CRÉATION DES MONSTRES (AKATSUKI & BOSS)
    # ==========================================
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
    
    # ==========================================
    # 5. ENREGISTREMENT EN BASE DE DONNÉES
    # ==========================================
    # insert_many permet d'envoyer toute la liste d'un coup.
    db.heroes.insert_many(heroes)
    db.monsters.insert_many(monsters)
    
    # 6. CONFIRMATION
    print("✅ SUCCÈS : Base de données Naruto mise à jour !")
    print(f" -> {len(heroes)} Héros de Konoha ajoutés.")
    print(f" -> {len(monsters)} Ennemis de l'Akatsuki ajoutés.")

# Cette partie permet de ne lancer le script que si on l'exécute directement
if __name__ == "__main__":
    init_db()