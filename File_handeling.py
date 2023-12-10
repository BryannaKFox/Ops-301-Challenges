# Script:                       ops301d10-challenge 10
# Author:                       Bryanna Fox
# Date of latest revision:      12/10/2023
# Purpose:                      File Handeling 

# Define the file name
file_name = "topsecret.txt"

# Step 1: Create a new .txt file and append three lines
with open(file_name, "w") as file:
    file.write("This is tope secret information.\n")
    file.write("Delete after reading.\n")
    file.write("You are awesome! \n")

# Step 2: Read and print the first line
with open(file_name, "r") as file:
    first_line = file.readline()
    print("First Line:", first_line)

# Step 3: Delete the .txt file
import os
os.remove(file_name)

# Inform the user that the file has been deleted
print(f"{file_name} has been deleted.")
