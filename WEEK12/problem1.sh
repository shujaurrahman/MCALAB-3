#!/bin/bash

# Shell script to back up a directory to a specified location

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 source_directory backup_location"
  exit 1
fi

# Set source and destination directories from the input arguments
SOURCE_DIR=$1
BACKUP_DIR=$2

# Get the current date and time for the backup filename
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_NAME="backup_$TIMESTAMP.tar.gz"

# Create a backup
echo "Creating backup of $SOURCE_DIR at $BACKUP_DIR/$BACKUP_NAME..."
tar -czf "$BACKUP_DIR/$BACKUP_NAME" "$SOURCE_DIR"

# Check if the backup was successful
if [ $? -eq 0 ]; then
  echo "Backup created successfully at $BACKUP_DIR/$BACKUP_NAME"
else
  echo "Backup failed"
  exit 1
fi
