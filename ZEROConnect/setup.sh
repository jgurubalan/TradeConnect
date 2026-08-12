#!/usr/bin/env bash

set -e

# Get project name from current directory
PROJECT_NAME=$(basename "$PWD")
PROJECT_NAME_LOWER=$(echo "$PROJECT_NAME" | tr '[:upper:]' '[:lower:]')

# Define virtual environment location
VENV_ROOT="$HOME/.venv"
VENV_DIR="$VENV_ROOT/.venv_$PROJECT_NAME_LOWER"

echo "Project: $PROJECT_NAME"
echo "Virtual environment: $VENV_DIR"

# Create root venv directory if it doesn't exist
mkdir -p "$VENV_ROOT"

# Create virtual environment if it doesn't already exist
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
else
    echo "Virtual environment already exists."
fi

# Activate virtual environment
source "$VENV_DIR/bin/activate"

# Upgrade pip
echo "Upgrading pip..."
python -m pip install --upgrade pip

# Install dependencies if requirements.txt exists
if [ -f requirements.txt ]; then
    echo "Installing requirements..."
    python -m pip install -r requirements.txt
else
    echo "No requirements.txt found. Skipping dependency installation."
fi

# Create VS Code settings directory
mkdir -p .vscode

# Configure VS Code to use this virtual environment
cat > .vscode/settings.json <<EOF
{
    "python.defaultInterpreterPath": "$VENV_DIR/bin/python"
}
EOF

echo
echo "========================================"
echo "Setup complete!"
echo "Project: $PROJECT_NAME"
echo "Virtual environment: $VENV_DIR"
echo
echo "To activate manually in the future, run:"
echo "source \"$VENV_DIR/bin/activate\""
echo "========================================"