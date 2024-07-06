# Flashcard Terminal Application - Pseudeocode

## Flashcard.py 
### Flashcard Class representing a single flashcard with a question and answer
class Flashcard:
    attributes: question, answer

### Deck Class representing a deck of flashcards
class Deck:
    attributes: name, flashcards (list)

### DeckManager Class managing decks and flashcards, handling creation, deletion, and operations
class DeckManager:
    attributes: decks (dictionary), filename

    method __init__:
        load_decks()  # Load existing decks from file

    method create_deck(name: str):
        Create a new deck with the specified name

    method delete_deck(name: str):
        Delete the specified deck
    
    method get_deck(name: str):
        Return the deck object for the given name

    method save_decks():
        Save the current decks to a file

    method quiz(deck_name: str):
        Shuffle, quiz, score, and review flashcards in the selected deck
