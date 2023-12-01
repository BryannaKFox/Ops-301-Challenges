#!/bin/bash

# Script:                       ops301d10-challenge 04
# Author:                       Bryanna Fox
# Date of latest revision:      11/30/2023
# Purpose:                      Conditionals in Menu Systems


while true; do
    clear
    echo "Menu:"
    echo "1. Hello world"
    echo "2. Ping self"
    echo "3. IP info"
    echo "4. Exit"

    read -p "Choose an option (1-4): " choice

    case $choice in
        1)
            echo "Hello world!"
            ;;
        2)
            ping -c 4 127.0.0.1
            ;;
        3)
            ifconfig
            ;;
        4)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid option. Please choose a number between 1 and 4."
            ;;
    esac

    read -p "Press enter to continue..."
done
