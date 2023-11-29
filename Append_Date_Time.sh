#!/bin/bash

# Script:                       ops301d10-challenge 02
# Author:                       Bryanna Fox
# Date of latest revision:      11/28/2023
# Purpose:                      Append; Date and Time


# Set the source and destination file paths
source_file="/var/log/syslog"
destination_file="samplesyslog.log"
current_date_time=$(date +"%m-%d-%Y")

# Copy the syslog file to the current working directory
cp "$source_file" "$destination_file"

# Display a message indicating the copy is complete
echo "SampleSyslog copied to $destination_file"

# Append content to file
echo "Appended to add the date: $(date +$%m-%d-%Y)" >> samplesyslog.log
