# Pulling from flashcard package
from flashcard import create_deck, delete_deck, select_deck, add_flashcard, view_flashcard, quiz

def main():
    # Main function to display the menu and handle user input
    current_deck = None
    # Loop until the user chooses to exit
    while True:
        # Display the menu
        print("\nFlashcard Application:")
        