#!/bin/bash


# Script:                       ops301d10-challenge 03
# Author:                       Bryanna Fox
# Date of latest revision:      11/29/2023
# Purpose:                      File Permissions

# Prompt user for input directory path
read -r "Enter the directory path: " directory_path

# Prompt user for input permissions number
read -r "Enter the permissions number (e.g., 777): " permissions

# Navigate to the input directory
cd "$directory_path" || exit

# Change permissions of all files in the directory
chmod -R "$permissions" /*

# Print directory contents and new permissions
echo -e "\nDirectory Contents:"
find . -maxdepth 1 -exec ls -l {} \;

echo -e "\nNew Permissions Setting:"
find . -maxdepth 1 -printf "%m %f\n"
