#!/bin/bash

# Commit and push changes for all directories

# 0x00-python_variable_annotations
cd 0x00-python_variable_annotations
git add .
read -p "Enter commit message for 0x00-python_variable_annotations: " commit_message_0x00
git commit -m "$commit_message_0x00"
git push origin main  # Assuming 'main' is your main branch name, change it if necessary
cd ..

# 0x01-python_async_function
cd 0x01-python_async_function
git add README.md
read -p "Enter commit message for 0x01-python_async_function: " commit_message_0x01
git commit -m "$commit_message_0x01"
git push origin main  # Assuming 'main' is your main branch name, change it if necessary
cd ..

# Main project directory
git add .
read -p "Enter commit message for the main project directory: " commit_message_main
git commit -m "$commit_message_main"
git push origin main  # Assuming 'main' is your main branch name, change it if necessary

