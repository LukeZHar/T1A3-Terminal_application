#!/bin/bash

# Check if python is installed
echo "Checking if Python is installed..."
python3 check_python.py

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
    echo "Tests passed. Exiting test..."
    
else
    echo "Tests failed. Exiting test..."
    exit 1
fi

# Deactivate the virtual environment
echo "Deactivating virtual environment..."
deactivate