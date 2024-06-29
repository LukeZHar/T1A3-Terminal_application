import os
import random
import json

base_dir = "decks"

# Ensure the base directory exists
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

def get_deck_file(deck_name):
    return os.path.join(base_dir, f"{deck_name}.json")

def load_deck(deck_name):
    deck_file = get_deck_file(deck_name)
    if not os.path.exists(deck_file):
        with open(deck_file, "r") as file:
            return json.load(file)
    return []

def save_deck(deck_name, deck):
    deck_file = get_deck_file(deck_name)
    with open(deck_file, "w") as file:
        json.dump(deck, file)

def list_decks():
    return [f.replace(".json", "") for f in os.listdir(base_dir) if f.endswith(".json")]

def create_deck(deck_name):
    deck_name = input("Enter deck name: ").strip()
    if deck_name and deck_name not in list_decks():
        save_deck(deck_name, [])
        print(f"Deck '{deck_name}' created.")
    else:
        print("Deck already exists.")

