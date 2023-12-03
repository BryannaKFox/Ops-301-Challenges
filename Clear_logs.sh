#!/bin/bash

# Script:                       ops301d10-challenge 05
# Author:                       Bryanna Fox
# Date of latest revision:      12/02/2023
# Purpose:                      Clear Logs

# Set the backup directory
backup_dir="/var/log/backups"

# Ensure the backup directory exists
mkdir -p "$backup_dir"

# Function to get the current timestamp
get_timestamp() {
  date +"%Y%m%d%H%M%S"
}

# Compress log files
compress_log() {
  log_file="$1"
  timestamp=$(get_timestamp)
  compressed_file="$backup_dir/$(basename "$log_file")-$timestamp.zip"
  
  # Print original file size
  original_size=$(du -h "$log_file" | cut -f1)
  echo "Original size of $log_file: $original_size"

  # Compress the log file
  gzip -c "$log_file" > "$compressed_file"

  # Clear the contents of the log file
  true > "$log_file"

  # Print compressed file size
  compressed_size=$(du -h "$compressed_file" | cut -f1)
  echo "Compressed size of $compressed_file: $compressed_size"

  # Print the compared sizes
  echo "Size comparison:"
  echo "  Original size:   $original_size"
  echo "  Compressed size: $compressed_size"
}

# Compress syslog
compress_log "/var/log/syslog"

# Compress wtmp
compress_log "/var/log/wtmp"
