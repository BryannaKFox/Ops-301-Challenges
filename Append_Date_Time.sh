#!/bin/bash

# Script:                       ops301d10-challenge 02
# Author:                       Bryanna Fox
# Date of latest revision:      11/28/2023
# Purpose:                      Append; Date and Time


# Set the source and destination file paths
source_file="/var/log/syslog"
destination_file="samplesyslog.log"

# Copy the syslog file to the current working directory
cp "$source_file" "$destination_file"

# Display a message indicating the copy is complete
echo "SampleSyslog copied to $destination_file"

# Append the current date to the end of the file name
new_destination_file="${destination_file%.log}-$(date +%m-%d-%Y).log"
mv "$destination_file" "$new_destination_file"

