# Flashcard application Help Documentation

## Installation Steps (simple version):

1. Clone Repository:

   - Open your terminal
   - Run this command to clone the repository: 'git clone https://github.com/LukeZHar/T1A3-Terminal_application.git'

2. Cd into the cloned directory:

   - Cd into T1A3-Terminal_application/src

3. Run chmod to make the script executable

   - Run this command: chmod +x run_setup.sh
   - Also this command: chmod +x run_app.sh

4. Run the 1st sh command in terminal

   - While still in src
   - Run this command: './run_setup.sh
   - It will check your system for python/python3
   - It will then start a virtual environment
   - It will check your system for what is outlined in 'requirements.txt'
   - It will download pytest and emoji if you don't have it already
   - It will run a test on a few features that are in 'test_flashcard.py'
   - Then it will exit

5. Next run the next sh command
   - It will start virtual environment
   - Then will run the application
   - Once done it will exit application

---

## Second option for setting up (Longer version):

1. Clone Repository:

   - Open your terminal
   - Run this command to clone the repository: 'git clone https://github.com/LukeZHar/T1A3-Terminal_application.git'
   - Cd into the repository "cd T1A3-Terminal_application/src

2. Activate Virtual Environments

   - On your terminal enter one of the following, depending on your system.
   - Unix/MacOs: 'source venv/bin/activate'
   - Windows: 'venv/Scripts/activate

3. Check for python
   
   - Run this command 'python3 check_python.py

3. Install Dependicies:

   - In your terminal while still in src run 'pip install -r requirements.txt'

4. Usage instructions:

   - Running the application:
     - In the terminal run: 'python3 main.py'

5. Navigating the application

   - Create Deck: Choose 1 to create a new deck with a name of your choice
   - Delete Deck: Choose 2 to Delete an existing deck
   - Select Deck: Choose 3 to Select a deck from the list shown
   - Add Flashcard: Choose 4 to add a flashcard to the deck you have chosen, otherwise it will ask you to choose a deck first
   - View Flashcard: Choose 5 to View your current flashcard in the deck your in
   - Quiz: Choose 6 to start a quiz with your flashcards in your current selected deck, flashcards will be shuffled
   - Exit: choose 7 to Exit the terminal application

---

## Aditional information

Dependencies:

- Python >= 3.6
- Pytest
- Emoji

System/Hardware requirements:

- Operating system: Windows/Linux/MacOS
- Python 3.6 or higher
- Some memory and storage for running python
