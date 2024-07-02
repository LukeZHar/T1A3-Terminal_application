# Pulling from flashcard package
import flashcard
from flashcard import create_deck, delete_deck, select_deck, add_flashcard, view_flashcard, quiz
def main():
    # Main function to display the menu and handle user input
    current_deck = None
    # Loop until the user chooses to exit
    while True:
        # Display the menu
        print("\nFlashcard Application:")
        print("1. Create Deck")
        print("2. Delete Deck")
        print("3. Select Deck")
        print("4. Add Flashcard")
        print("5. View Flashcard")
        print("6. Quiz")
        print("7. Exit")
        # Get user input
        choice = input("Enter your choice: ").strip()
        # Handle user input
        # Create deck
        if choice == "1":
            create_deck()
        # Delete deck
        elif choice == "2":
            delete_deck()
        # Select deck
        elif choice == "3":
            current_deck = select_deck()
        # Add flashcard
        elif choice == "4":
            if current_deck:
                add_flashcard(current_deck)
            else:
                print("Please select a deck first.")
        # View flashcard
        elif choice == "5":
            if current_deck:
                view_flashcard(current_deck)
            else:
                print("Please select a deck first.")
        # Quiz
        elif choice == "6":
            if current_deck:
                quiz(current_deck)
            else:
                print("Please select a deck first.")
        # Exit
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

# Call the main function to start the application
if __name__ == "__main__":
    main()
