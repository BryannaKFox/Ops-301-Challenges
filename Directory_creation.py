# Script:                       ops301d10-challenge 07
# Author:                       Bryanna Fox
# Date of latest revision:      12/04/2023
# Purpose:                      Directory Creation

#!/usr/bin/env python3

# Import libraries
import os

# Declaration of variables
user_path = input('Enter the directory path:')

# Declaration of functions
def generate_directory_structure(user_path):
    
     
    for (root, dirs, files) in os.walk(user_path):
        # Add a print command here to print ==root==
        print(f'Root directory:{root}')
            
         # Add a print command here to print ==dirs==
        print(f'Sub-directories:{dirs}')
                
        # Add a print command here to print ==files==
        print(f'Files:{files}')


# Main

# Pass the variable into the function here
generate_directory_structure(user_path)

# End
