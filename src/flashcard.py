import os
import random
import json

# Directory for the deck storage
base_dir = "decks"

# Ensure the base directory exists at startup
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

# Get the full path to the deck file
def get_deck_file(deck_name):
    # Constructs the full path to the deck file
    return os.path.join(base_dir, f"{deck_name}.json")

# Loads the deck from the JSON file
def load_deck(deck_name):
    deck_file = get_deck_file(deck_name)
    # Check if the deck file exists
    if not os.path.exists(deck_file):
        with open(deck_file, "r") as file:
            return json.load(file)  
    return []

# Saves the deck to the JSON file
def save_deck(deck_name, deck):
    deck_file = get_deck_file(deck_name)
    try:    
        with open(deck_file, "w") as file:
            json.dump(deck, file)
    # Catch any exceptions and print an error message
    except Exception as e:
        print(f"Failed to save deck: {e}")

# Lists all the decks
def list_decks():
    return [f.replace(".json", "") for f in os.listdir(base_dir) if f.endswith(".json")]

# Creates a new deck
def create_deck(deck_name):
    deck_name = input("Enter deck name: ").strip()
    if deck_name and deck_name not in list_decks():
        save_deck(deck_name, [])
        print(f"Deck '{deck_name}' created.")
    # Check if the deck already exists
    else:
        print("Deck already exists.")

# Deletes a deck
def delete_deck(deck_name):
    deck_name = input("Enter deck name: ").strip()
    deck_file = get_deck_file(deck_name)
    # Check if the deck file exists
    if os.path.exists(deck_file):
        os.remove(deck_file)
        print(f"Deck '{deck_name}' deleted.")
    # Check if the deck file does not exist
    else:
        print("Deck does not exist.")

# Selects a deck
def select_deck():
    decks = list_decks()
    if not decks:
        print("No decks found. Create one first.")
        return None
    # Select a deck
    print("Select a deck:")
    # Print the list of decks
    for i, deck in enumerate(decks, 1):
        print(f"{i}. {deck}")
    # Get the user's choice
    choice = input("Enter the deck number to choose: ").strip()
    # Check if the choice is valid
    if choice.isdigit() and 1 <= int(choice) <= len(decks):
        return decks[int(choice) - 1]
    print("Invalid choice.")
    return None

# Adds a flashcard
def add_flashcard(deck_name, question=None, answer=None):
    # Allows input of question and answer
    if not question:
        question = input("Enter the question: ").strip()
    if not answer:
        answer = input("Enter the answer: ").strip()
    if question and answer:
        # Add the flashcard to the deck
        deck = load_deck(deck_name)
        deck.append({"question": question, "answer": answer})
        save_deck(deck_name, deck)
        print(f"Flashcard added to deck '{deck_name}'.")
    else:
        print("Question and answer cannot be empty.")

# View a flashcard
def view_flashcard(deck_name):
    deck = load_deck(deck_name)
    if deck:
        for i, flashcard in enumerate(deck, 1):
            print(f"{i}. {flashcard['question']} - {flashcard['answer']}")
    else:
        print("No flashcards found in deck.")
