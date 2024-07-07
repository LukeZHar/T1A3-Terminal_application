# Flashcard Terminal Application - Pseudeocode

## Flashcard.py 
### Flashcard Class representing a single flashcard with a question and answer
- class Flashcard:
    - attributes: question, answer

### Deck Class representing a deck of flashcards
- class Deck:
    - attributes: name, flashcards (list)

### DeckManager Class managing decks and flashcards, handling creation, deletion, and operations
- class DeckManager:
    - attributes: decks (dictionary), filename

    - method __init__:
        - load_decks()  
        "Loads existing decks from file"

    - method create_deck(name: str):
        - Create a new deck with the specified name

    - method delete_deck(name: str):
        - Delete the specified deck
    
    - method get_deck(name: str):
        - Return the deck object for the given name

    - method save_decks():
        - Save the current decks to a file

    - method quiz(deck_name: str):
        - Shuffle, quiz, score, and review flashcards in the selected deck

## main.py
### Import necessary functions and classes from flashcard.py
- def main():
    - deck_manager = DeckManager()  
    "Initialize DeckManager"

    - while True:  "Main menu loop"
        - print_menu_options()
        - choice = get_user_choice()

        - if choice == "1":
            - deck_manager.create_deck(name)
        - elif choice == "2":
            - deck_manager.delete_deck(name)
        - elif choice == "3":
            - current_deck = deck_manager.get_deck(name)
        - elif choice == "4":
            - if current_deck:
                - add_flashcard()
            - else:
                - display_error("Please select a deck first.")
        - elif choice == "5":
            - if current_deck:
                - view_flashcards(current_deck)
            - else:
                - display_error("Please select a deck first.")
        - elif choice == "6":
            - if current_deck:
                - correct, incorrect = deck_manager.quiz(current_deck.name)
            - else:
                - display_error("Please select a deck first.")
        - elif choice == "7":
            - exit()
        - else:
            - display_error("Invalid choice. Please try again.")

## test_flashcard.py 
### Import the pytest module and necessary classes from flashcard.py
- import pytest
- from flashcard import Deck, Flashcard, DeckManager

### Test the creation of a deck
- def test_create_deck():  
    
    "Initialize DeckManager"
    - deck_manager = DeckManager()

    "Create a new deck named "Test Deck""
    - deck_manager.create_deck('Test Deck')

    "Assert that the deck is created and exists in DeckManager's decks"
    - assert 'Test Deck' in deck_manager.decks

### Test adding a flashcard to a deck
- def test_add_flashcard():
    
    "Initialize a deck with the name "Test Deck""
    - deck = Deck('Test Deck')

    "Initialize a flashcard with a question and answer"
    - flashcard = Flashcard('Question?', 'Answer.')

    "Add the flashcard to the deck"
    - deck.add_flashcard(flashcard)

    "Assert that the flashcard is added to the deck"
    - assert len(deck.flashcards) == 1

### Test saving and loading decks
- def test_save_load_decks(tmp_path):
    "Create a temporary file path for decks.json"
    - test_file = tmp_path / "decks.json"

    "Initialize DeckManager with the temporary file path"
    - deck_manager = DeckManager(filename=test_file)

    "Create a new deck named "Test Deck""
    - deck_manager.create_deck('Test Deck')

    "Save the decks to the temporary file"
    - deck_manager.save_decks()

    "Initialize a new DeckManager to load the saved decks"
    - new_manager = DeckManager(filename=test_file)

    "Assert that the deck "Test Deck" exists in the new DeckManager's decks"
    - assert 'Test Deck' in new_manager.decks

### Main function to run the tests
- if __name__ == "__main__":
    - pytest.main()