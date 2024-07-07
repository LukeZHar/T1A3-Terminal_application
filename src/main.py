# Import emoji library
import emoji
# import from flashcard.py
from flashcard import Flashcard, Deck, DeckManager

# main function
def main():
    deck_manager = DeckManager()  # Initialize the Deck Manager
    current_deck = None # Variable to store the current deck

    # Main menu loop
    while True:
        
        # Display the main menu
        try:
            print("\nFlashcard Application:")
            print(emoji.emojize("1. Create Deck :open_book:"))
            print(emoji.emojize("2. Delete Deck :wastebasket:"))
            print(emoji.emojize("3. Select Deck :books:"))
            print(emoji.emojize("4. Add Flashcard :memo:"))
            print(emoji.emojize("5. View Flashcards :eyes:"))
            print(emoji.emojize("6. Quiz :game_die:"))
            print(emoji.emojize("7. Exit :door:"))
            
            # Get input
            choice = input("Enter your choice: ").strip()

            # Process input into create deck
            if choice == "1":
                deck_name = input("Enter deck name: ")
                deck_manager.create_deck(deck_name)
                deck_manager.save_decks()
                print(emoji.emojize("Deck created successfully. :check_mark:"))
            
            # Process input into delete deck
            elif choice == "2":
                deck_name = input("Enter deck name to delete: ")
                deck_manager.delete_deck(deck_name)
                deck_manager.save_decks()
                print(emoji.emojize("Deck deleted successfully. :litter_in_bin_sign:"))

            # Process input into select deck
            elif choice == "3":
                # List all available decks
                print("\nAvailable Decks:")
                for deck_name in deck_manager.decks.keys():
                    print(deck_name)
                deck_name = input("Enter the deck name you want to select: ")
                current_deck = deck_manager.get_deck(deck_name)
                print(emoji.emojize(f"Selected deck: {current_deck.name} :thumbs_up:"))

            # Process input into add flashcard
            elif choice == "4":
                if current_deck:
                    # Asks for question and answer
                    question = input("Enter the question: ")
                    answer = input("Enter the answer: ")
                    current_deck.add_flashcard(Flashcard(question, answer))
                    deck_manager.save_decks()
                    print(emoji.emojize("Flashcard added successfully. :sparkles:"))
                # If no deck is selected
                else:
                    print(emoji.emojize("Please select a deck first. :warning:"))

            # Process input into view flashcards
            elif choice == "5":
                if current_deck:
                    for idx, card in enumerate(current_deck.flashcards, 1):
                        print(f"{idx}. Question: {card.question}, Answer: {card.answer}")
                # If no deck is selected
                else:
                    print(emoji.emojize("Please select a deck first. :warning:"))          

            # Process input into quiz
            elif choice == "6":
                if current_deck:
                    correct, incorrect = deck_manager.quiz(current_deck.name)
                    print(emoji.emojize(f"Quiz Complete! Correct: {correct} :check_mark:, Incorrect: {incorrect} :cross_mark:"))
                # If no deck is selected
                else:
                    print(emoji.emojize("Please select a deck first. :warning:"))

            # Process input into exit
            elif choice == "7":
                print(emoji.emojize("Goodbye! :waving_hand:"))
                exit()

            # Invalid choice if anything else is put in
            else:
                print(emoji.emojize("Invalid choice. Please try again. :warning:"))
        
        # Exception handling
        except Exception as e:
            print(emoji.emojize(f"An error occurred: {e} :double_exclamation_mark:"))

# Run the main function
if __name__ == "__main__":
    main()

