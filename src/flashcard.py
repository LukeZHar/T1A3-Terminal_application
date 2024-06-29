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

def delete_deck(deck_name):
    deck_name = input("Enter deck name: ").strip()
    deck_file = get_deck_file(deck_name)
    if os.path.exists(deck_file):
        os.remove(deck_file)
        print(f"Deck '{deck_name}' deleted.")
    else:
        print("Deck does not exist.")

def select_deck():
    decks = list_decks()
    if not decks:
        print("No decks found. Create one first.")
        return None
    print("Select a deck:")
    for i, deck in enumerate(decks, 1):
        print(f"{i}. {deck}")
    choice = input("Enter the deck number to choose: ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(decks):
        return decks[int(choice) - 1]
    print("Invalid choice.")
    return None

def add_flashcard(deck_name):