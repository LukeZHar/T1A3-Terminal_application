#!/bin/bash

# Create a virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Running the application
echo "Running the application..."
python3 main.py

# Deactivate the virtual environment
echo "Deactivating virtual environment..."
deactivate
