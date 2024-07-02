# Flashcard Terminal Application - Pseudeocode

## Start of program
1. Define base dir as decks.
2. Ensure that the base dir exists, if not create it.

## Helper functions
### Function get deck file:
- Return the file path by combining base dir and deckname with .json.

### Function load deck
- Get file path using get deck file
- If the file exists, open and read JSON data, then return it
- If the file does not exist return an empyt list

### Function save deck
- Get file path using get deck file
- Open the file and save JSON data from deck

### Function list deck
- List all files in base dir
- Filter and return list of deck names without "json" extesnion

## Feature Functions
### Function create deck
- Prompt for a new deckname
- If deckname is not empty and doesn't exist in list deck
    - call on save deck funtion
    - Prompt that deck has been created
- Else, prompt that deck already exists or name is invalid

### Function delete deck
- Prompts to enter the name of deck to delete 
- gets file path using get deck file
- if the file exists, deletes it 
- Prompts that deck is deleted
- Else prompt that deck doesn't exist

### Function Add flashcard
- Prompts for a question and answer 
- If both are not blank:
    - Loads deck using load deck
    - Add new flashcard (Question and Answer) to the deck
    - Save updated deck using save deck
    - Prompt that flashcard was added
- Else prompts both inputs can't be empty

### Function view flashcard
- Load deck using load deck
- If the deck has flashcards
    - Loop through the flashcards showing the question and answers

### Function Quiz
- Load deck using load deck
- If the deck has flashcards
    - Shuffle the deck
    - Starts correct and incorrect counter
    - Starts a result list to store quiz data 
    - Loop through flashcards
        - Display the question
        - Prompt for an answer
        - Compare with the correct answer
        - Update the Correct and incorrect counter
        - Update question, answer and correct answer to results
    - Display the final score (Coorect/total questions)
    - Calls the review result function for review mode

### Function Review results
- Loop through each item in results
    - Display question, answer given and correct answer

## Main function
### Function main
- Set current deck as none
- Loop until user chooses to exit
    - Display main menu 
        1. Create Deck
        2. Delete Deck
        3. Select Deck
        4. Add Flashcard
        5. View Flashcards
        6. Quiz
        7. Exit
    - Prompt for choice
    - If choice is 1
        - Call create deck
    - If choice is 2
        - Call Delete deck
    - If choice is 3
        - Set current deck through select deck
    - If choice is 4 
        - If current deck is not none, call add flashcards
        - Else, prompt to select a deck first
    - If choice is 5
        - If current deck is not none, call view flashcards
        - Else, prompt to select a deck first 
    - If choice is 6 
        - If cuurent deck is not none, call quiz
        - Else, prompt to select a deck first
    - If choice is 7
        - Break the loop to exit
    - Else prompt to choose a valid option

End program
