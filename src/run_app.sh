#!/bin/bash

# Check if python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python is not installed. Please install Python and try again."
    exit 1
fi

# Create a virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run the tests
echo "Running tests..."
pytest test_flashcard.py

# Check if tests passed
if [ $? -eq 0 ]
then
    echo "Tests passed. Exiting..."
    
else
    echo "Tests failed. Exiting..."
    exit 1
fi

# Running the application
echo "Running the application..."
python3 main.py

# Deactivate the virtual environment
echo "Deactivating virtual environment..."
deactivate
