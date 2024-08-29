#!/bin/bash
SCRIPT_DIR="$(dirname "$(realpath "$0")")"
PYTHON_SCRIPT="$SCRIPT_DIR/main.py"

echo "Installing the Colorama library..."
pip install colorama

ALIAS_COMMAND="alias tasks='python3 $PYTHON_SCRIPT'"

if [ -f ~/.zshrc ]; then
  if grep -q "$ALIAS_COMMAND" ~/.zshrc; then
    echo "Zsh alias already exists."
  else
    echo "$ALIAS_COMMAND" >> ~/.zshrc
    echo "Zsh alias added. Please restart the terminal or run 'source ~/.zshrc'."
  fi
fi

if [ -f ~/.bashrc ]; then
  if grep -q "$ALIAS_COMMAND" ~/.bashrc; then
    echo "Bash alias already exists."
  else
    echo "$ALIAS_COMMAND" >> ~/.bashrc
    echo "Bash alias added. Please restart the terminal or run 'source ~/.bashrc'."
  fi
fi

if [ -f ~/.bash_profile ]; then
  if grep -q "$ALIAS_COMMAND" ~/.bash_profile; then
    echo "Bash profile alias already exists."
  else
    echo "$ALIAS_COMMAND" >> ~/.bash_profile
    echo "Bash profile alias added. Please restart the terminal or run 'source ~/.bash_profile'."
  fi
fi
