# imports for this module
import json
import os
import random

# class for flashcard
class Flashcard:
    def __init__(self, question: str, answer: str):
        # Initialize flashcard with question and answer
        self.question = question
        self.answer = answer

# class for deck
class Deck:
    def __init__(self, name: str):
        # Initialize deck with name and an empty list of flashcards
        self.name = name
        self.flashcards = []

    # Add flashcard to deck
    def add_flashcard(self, flashcard: Flashcard):
        self.flashcards.append(flashcard)

    # Convert deck to dictionary with a JSON-compatible format
    def to_dict(self):
        return {"name": self.name, "flashcards": [{"question": fc.question, "answer": fc.answer} for fc in self.flashcards]}


    @staticmethod
    def from_dict(deck_dict):
        # Convert deck dictionary to deck object
        deck = Deck(deck_dict["name"])
        for fc_dict in deck_dict["flashcards"]:
            deck.add_flashcard(Flashcard(fc_dict["question"], fc_dict["answer"]))
        return deck

# class for deck manager
class DeckManager:
    def __init__(self, filename='decks.json'):
        #Initialize deck manager with a list of decks and a filename
        self.decks = {}
        self.filename = filename
        self.load_decks()

    # Create a new deck
    def create_deck(self, name):
        # Check if deck with this name already exists
        if name in self.decks:
            raise ValueError("Deck with this name already exists.")
        # Add deck to deck manager
        self.decks[name] = Deck(name)

    # Delete a deck
    def delete_deck(self, name):
        # Check if deck with this name exists
        if name not in self.decks:
            raise ValueError("Deck not found.")
        # Remove deck from deck manager
        del self.decks[name]

    # Get a deck
    def get_deck(self, name):
        # Check if deck with this name exists
        if name not in self.decks:
            raise ValueError("Deck not found.")
        # Return deck
        return self.decks[name]

    # Save decks to file
    def save_decks(self):
        try:
            with open(self.filename, 'w') as f:
                json.dump([deck.to_dict() for deck in self.decks.values()], f, indent=4)
        # Print error message if saving fails
        except IOError as e:
            print(f"Error saving decks to {self.filename}: {e}")

    # Load decks from file
    def load_decks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    decks_list = json.load(f)
                    self.decks = {deck_dict["name"]: Deck.from_dict(deck_dict) for deck_dict in decks_list}
            # Print error message if loading fails
            except (IOError, json.JSONDecodeError) as e:
                print(f"Error loading decks from {self.filename}: {e}")

    # Start a quiz
    def quiz(self, deck_name):
        # Get deck
        deck = self.get_deck(deck_name)
        flashcards = deck.flashcards.copy()
        # Shuffle flashcards
        random.shuffle(flashcards)  

        # starting score set
        correct = 0
        incorrect = 0
        for card in flashcards:
            print(f"Question: {card.question}")
            user_answer = input("Your answer: ").strip()
            
            # Compare answer to correct answer
            if user_answer.lower() == card.answer.lower():  # Case-insensitive comparison
                correct += 1
                print("Correct!")
            # If answer is incorrect
            else:
                incorrect += 1
                print(f"Incorrect. The correct answer is: {card.answer}")
        
        # Print final score
        return correct, incorrect  
    