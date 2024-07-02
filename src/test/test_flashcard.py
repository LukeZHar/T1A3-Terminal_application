import os 
import pytest
from src.flashcard import base_dir, get_deck_file, save_deck, load_deck, list_decks, add_flashcard

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
