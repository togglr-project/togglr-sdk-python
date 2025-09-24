#!/bin/bash
# Install development dependencies for togglr-sdk-python

set -e

echo "Installing development dependencies..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -e .

# Install development dependencies
echo "Installing development dependencies..."
pip install pytest pytest-cov black isort flake8 mypy

# Install openapi-generator-cli for client generation
echo "Installing openapi-generator-cli..."
pip install openapi-generator-cli

echo "Installation complete!"
echo "To activate the virtual environment, run: source venv/bin/activate"
echo "To run tests, run: make test"
echo "To generate client, run: make generate"
