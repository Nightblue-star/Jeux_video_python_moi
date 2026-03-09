import sys
import time
from pymongo import MongoClient, DESCENDING

def main():
    while True:
        print("1. Nouvelle Mission")
        print("2. Voir le Bingo Book")
        print("3. Quitter")
        