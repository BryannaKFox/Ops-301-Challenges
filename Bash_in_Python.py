# Script:                       ops301d10-challenge 06
# Author:                       Bryanna Fox
# Date of latest revision:      12/04/2023
# Purpose:                      Bash in Python

# Declaring Variables
user = 'Mario'
location = 'New York'
job = 'plumber'

#Print the user and his information
print; 'The name of the new employee is' ; user
print; user; 'lives in' ; location
print; user; 'works as a' ; job 

#using os by importing it
import os

#Running bash commands through the imported os
os.system ('whoami')
os.system ('ip a')
os.system ('lshw -short')
