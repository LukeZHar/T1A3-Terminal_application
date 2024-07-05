from flashcard import Flashcard, Deck, DeckManager

def main():
    deck_manager = DeckManager()  # Initialize the Deck Manager
    current_deck = None

    while True:
        try:
            print("\nFlashcard Application:")
            print("1. Create Deck")
            print("2. Delete Deck")
            print("3. Select Deck")
            print("4. Add Flashcard")
            print("5. View Flashcards")
            print("6. Quiz")
            print("7. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                deck_manager.create_deck(input("Enter deck name: "))
                deck_manager.save_decks()
                print("Deck created successfully.")

            elif choice == "2":
                deck_manager.delete_deck(input("Enter deck name to delete: "))
                deck_manager.save_decks()
                print("Deck deleted successfully.")

            elif choice == "3":
                print("\nAvailable Decks:")
                for deck_name in deck_manager.decks.keys():
                    print(deck_name)
                selected_name = input("Enter the deck name you want to select: ")
                current_deck = deck_manager.get_deck(selected_name)
                print(f"Selected deck: {current_deck.name}")

            elif choice == "4":
                if current_deck:
                    question = input("Enter the question: ")
                    answer = input("Enter the answer: ")
                    current_deck.add_flashcard(Flashcard(question, answer))
                    deck_manager.save_decks()
                    print("Flashcard added successfully.")
                else:
                    print("Please select a deck first.")

            elif choice == "5":
                if current_deck:
                    for idx, card in enumerate(current_deck.flashcards, 1):
                        print(f"{idx}. Question: {card.question}, Answer: {card.answer}")
                else:
                    print("Please select a deck first.")                

            elif choice == "6":
                if current_deck:
                    correct, incorrect = deck_manager.quiz(current_deck.name)
                    print(f"Quiz Complete! Correct: {correct}, Incorrect: {incorrect}")
                else:
                    print("Please select a deck first.")

            elif choice == "7":
                exit()

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

