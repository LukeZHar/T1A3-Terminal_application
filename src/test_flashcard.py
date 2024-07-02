import os 
import pytest
from flashcard import base_dir, get_deck_file, save_deck, load_deck, list_decks, add_flashcard

@pytest.fixture
def setup_env():
    # Set up and tear down environment
    # Create a temporary directory
    if not os.path.exists(base_dir):
        os.mkdir(base_dir)
    yield
    # Tear down environment
    # Remove temporary directory
    for filename in os.listdir(base_dir):
        file_path = os.path.join(base_dir, filename)
        os.remove(file_path)
    os.rmdir(base_dir)

def test_create_and_load_deck(setup_env):
    # Test create deck and load deck
    deck_name = "test_deck"
    data = [{"Question": "test_question", "Answer": "test_answer"}]
    save_deck(deck_name, data)
    loaded_data = load_deck(deck_name)
    assert loaded_data == data

def test_list_decks(setup_env):
    # Test list decks
    deck_name1 = "test_deck"
    deck_name2 = "test_deck2"
    save_deck(deck_name1, [])
    save_deck(deck_name2, [])
    decks = list_decks()
    assert deck_name1 in decks
    assert deck_name2 in decks

def test_add_flashcard(setup_env):
    # Test add flashcard
    deck_name = "test_deck"
    save_deck(deck_name, [])
    add_flashcard(deck_name, "test_question", "test_answer")
    deck = load_deck(deck_name)
    assert len(deck) == 1
    assert deck[0] == ["Question"] == "test_question"
    assert deck[0] == ["Answer"] == "test_answer"

# Add more test cases as needed

# Call main() to run the tests
if __name__ == "__main__":
    pytest.main()