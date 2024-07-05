import json
import os
import random

class Flashcard:
    def __init__(self, question: str, answer: str):
        self.question = question
        self.answer = answer

class Deck:
    def __init__(self, name: str):
        self.name = name
        self.flashcards = []

    def add_flashcard(self, flashcard: Flashcard):
        self.flashcards.append(flashcard)

    def to_dict(self):
        return {"name": self.name, "flashcards": [{"question": fc.question, "answer": fc.answer} for fc in self.flashcards]}

    @staticmethod
    def from_dict(deck_dict):
        deck = Deck(deck_dict["name"])
        for fc_dict in deck_dict["flashcards"]:
            deck.add_flashcard(Flashcard(fc_dict["question"], fc_dict["answer"]))
        return deck

class DeckManager:
    def __init__(self, filename='decks.json'):
        self.decks = {}
        self.filename = filename
        self.load_decks()

    def create_deck(self, name):
        if name in self.decks:
            raise ValueError("Deck with this name already exists.")
        self.decks[name] = Deck(name)

    def delete_deck(self, name):
        if name not in self.decks:
            raise ValueError("Deck not found.")
        del self.decks[name]

    def get_deck(self, name):
        if name not in self.decks:
            raise ValueError("Deck not found.")
        return self.decks[name]

    def save_decks(self):
        try:
            with open(self.filename, 'w') as f:
                json.dump([deck.to_dict() for deck in self.decks.values()], f, indent=4)
        except IOError as e:
            print(f"Error saving decks to {self.filename}: {e}")

    def load_decks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    decks_list = json.load(f)
                    self.decks = {deck_dict["name"]: Deck.from_dict(deck_dict) for deck_dict in decks_list}
            except (IOError, json.JSONDecodeError) as e:
                print(f"Error loading decks from {self.filename}: {e}")

    def quiz(self, deck_name):
        deck = self.get_deck(deck_name)
        flashcards = deck.flashcards.copy()
        random.shuffle(flashcards)  # Shuffle flashcards

        correct = 0
        incorrect = 0
        for card in flashcards:
            print(f"Question: {card.question}")
            user_answer = input("Your answer: ").strip()

            if user_answer.lower() == card.answer.lower():  # Case-insensitive comparison
                correct += 1
                print("Correct!")
            else:
                incorrect += 1
                print(f"Incorrect. The correct answer is: {card.answer}")

        return correct, incorrect  