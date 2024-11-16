#!/bin/bash

# Script to search for a specific pattern in a file

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 pattern filename"
  exit 1
fi

# Assign input arguments to variables
PATTERN=$1
FILENAME=$2

# Check if the file exists
if [ ! -f "$FILENAME" ]; then
  echo "File '$FILENAME' not found."
  exit 1
fi

# Search for the pattern in the file
echo "Searching for pattern '$PATTERN' in file '$FILENAME':"
grep -n "$PATTERN" "$FILENAME"

# Check if any matches were found
if [ $? -ne 0 ]; then
  echo "No matches found for pattern '$PATTERN'."
else
  echo "Search completed."
fi
