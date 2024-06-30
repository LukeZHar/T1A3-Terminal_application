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
- 