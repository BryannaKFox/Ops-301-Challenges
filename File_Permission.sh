#!/bin/bash


# Script:                       ops301d10-challenge 03
# Author:                       Bryanna Fox
# Date of latest revision:      11/29/2023
# Purpose:                      File Permissions

# Prompt user for input directory path
read -p "Enter the directory path: " directory_path

# Prompt user for input permissions number
read -p "Enter the permissions number (e.g., 777): " permissions

# Navigate to the input directory
cd "$directory_path" || exit

# Change permissions of all files in the directory
chmod -R "$permissions" *

# Print directory contents and new permissions
echo -e "\nDirectory Contents:"
ls -l

echo -e "\nNew Permissions Setting:"
ls -l | awk '{print $1, $9}'
