import pytest
from flashcard import Deck, Flashcard, DeckManager

def test_create_deck():
    deck_manager = DeckManager()
    deck_manager.create_deck('Test Deck')
    assert 'Test Deck' in deck_manager.decks

def test_add_flashcard():
    deck = Deck('Test Deck')
    flashcard = Flashcard('Question?', 'Answer.')
    deck.add_flashcard(flashcard)
    assert len(deck.flashcards) == 1

def test_save_load_decks(tmp_path):
    test_file = tmp_path / "decks.json"
    deck_manager = DeckManager(filename=test_file)
    deck_manager.create_deck('Test Deck')
    deck_manager.save_decks()

    new_manager = DeckManager(filename=test_file)
    assert 'Test Deck' in new_manager.decks

if __name__ == "__main__":
    pytest.main()