# T1A3-Terminal_application
## General Documentation
- Title: Flashcard Terminal Application
- Author: Luke Harris
- End Date: 07/07/2024

## Help Documentation
- [Link to help doc](./docs/Help%20Doc/help_documentation.md)

## Pseudocode Document
- [Link to pseudocode doc](./docs/pseudocode/pseudocode.md)

## Source Control Repository
- [Link to Github Repository](https://github.com/LukeZHar/T1A3-Terminal_application)

## Code Style Guide
- Code Style PEP 8 - Style guide for Python Code
    - [Link to PEP 8 Reference website](https://peps.python.org/pep-0008/)

## Project Overview
This terminal application allows you to create and manage flashcards through the command line and then quiz yourself on the questions you provided. 

### Summary of code and files
- 'flashcards.py':
    - Defines classes 'Flashcard', 'Deck', and 'DeckManager' for managing flashcards and decks.
    - 'DeckManager' includes methods for creating and deleting, saving, loading decks, and running a quiz.
    - Includes error handling for file operations.

- 'main.py':
    - Contains the main loop for the interface, allowing you to interact with the flashcard system
    - Handles creating, deleteing, selecting decks, adding/viewing flashcards, and running the quiz
    - Ensures error handling for unexpected issues.

- 'test_flashcard.py':
    -  Contains tests for the 'Deck' and 'DeckManager' classes using pytest 

- 'decks.json' 
    - A JSON file containing data for decks and flashcards

- 'requirements.txt':
    - Lists dependecies required by the application

- 'run_app.sh':
    - A shell script for running the application, including activating the virtual environment if it exists

## Features and Functions
### Deck Management
#### Create Deck:  
- Description: Create a new deck. Input the deck name, verified to avoid duplicates, and then saves as a new JSON file.

- Logic: 
    - Prompts for a deck name.
    - Check if the deck name already exists.
    - If it does not exist, create a new JSON file for the deck.
    - If it does exist, asks for a different name.

#### Delete Deck:  
- Description: Delete an existing deck by specifying its name.

- Logic:
    - Prompts for the deck name.
    - Check if the deck exists in the directory.
    - If it exists, delete the JSON file.
    - If it does not exist, prompts name doesnt exist.

#### Select Deck
- Description: Select a deck to perform operations.

- Logic:
    - List all available decks.
    - Prompt to choose a deck by number.
    - Validates input and sets the current deck.


### Flashcard Creation
- Description: Add new flashcards to the selected deck by providing a question and an answer.

- Logic:
    - Prompts for a question and an answer.
    - Load the current deck from its JSON file.
    - Append the new flashcard to the deck.
    - Save the updated deck back to the JSON file.


### Quiz Mode
- Description: Shuffles flashcards then quizzes you, keeping track of correct and incorrect responses.

- Logic:
    - Load the selected deck.
    - Shuffle the order of flashcards.
    - Loop through each flashcard, prompting the user for an answer.
    - Track correct and incorrect answers.
    - Display the quiz score at the end.


### Scoring
- Description: Tracks the number of correct and incorrect answers during the quiz for the user to see their progress.

- Logic:
    - Maintain counters for correct and incorrect answers.
    - Update counters based on user’s responses during the quiz.


### Review
- Description: After completing a quiz session, you can review your answers and see where you need to improve.

- Logic:
    - Store each question, input, and correct answer during the quiz.
    - After the quiz, display all these results for review.

 
### Save and Load
- Description: Save flashcards and decks in JSON files to load them later.

- Logic:
    - Save: Convert the deck list to JSON format and write it to a file.
    - Load: Read the JSON file, parse it, and return the deck list.

## Implementation Plan
### Deck Management
1.1 Create Deck
- Tasks:
    - Setup project structure and directories.
    - Implement input prompt for deck name.
    - Check if deck already exists function.
    - Create new JSON file if not exists.
    - Add error handling for file operations.
  
Deadline: 01/07/2024

1.2 Delete Deck
- Tasks:
    - Implement input prompt for deck name.
    - Check if deck file exists.
    - Delete the JSON file.
    - Add error handling for file operations.
    - Confirm deletion.

Deadline: 01/07/2024

1.3 Select Deck
- Tasks:
    - List all existing decks function.
    - Implement input prompt for selecting a deck.
    - Validate user input.
    - Set selected deck to current working deck.
    - Confirm selection.

Deadline: 01/07/2024

### Flashcard Creation
2.1 Add Flashcard
- Tasks:
    - Implement input prompts for question and answer.
    - Load the selected deck from JSON file.
    - Append new flashcard to the deck.
    - Save updated deck back to JSON file.
    - Add error handling for file I/O operations.

Deadline: 02/07/2024

### Quiz
3.1 Implement Quiz
- Tasks:
    - Load the selected deck from JSON file.
    - Shuffle the order of flashcards.
    - Implement loop to iterate through flashcards.
    - Prompt for answers and check.
    - Track correct and incorrect answers.

Deadline: 03/07/2024

3.2 Scoring
- Tasks:
    - Count correct and incorrect responses.
    - Display results at the end of the quiz.
    - Test scoring with different decks.
    - Handle edge cases (e.g., empty deck).
    - Add error handling for unexpected inputs.

Deadline: 03/07/2024

### Review Mode
4.1 Implement Review Mode
- Tasks:
    - Store input during the quiz.
    - Implement function to display inputs and correct answers.
    - Format the output for review clarity.
    - Allow navigation through reviewed questions.
    - Handle various review scenarios (all correct and incorrect inputs).

Deadline: 04/07/2024

### Save and Load
5.1 Save and Load Decks
- Tasks:
    - Implement function to save the deck to JSON.
    - Implement function to load the deck from JSON.
    - Ensure data integrity during save/load.
    - Add error handling for file I/O operations.
    - Test save/load with large decks.

Deadline: 05/07/2024

### Trello Screenshots
![Trello board](./docs/Trello/Trello.png)
![Trello Tasks](./docs/Trello/trello-tasks.png)

- [Link to Trello Website as a reference](https://trello.com/)



