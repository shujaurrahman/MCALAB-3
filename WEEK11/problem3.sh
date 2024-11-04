#!/bin/bash

# Check if a number is provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <number>"
    exit 1
fi

# Store the number from the argument
NUMBER=$1

# Check if the input is a valid integer
if ! [[ "$NUMBER" =~ ^-?[0-9]+$ ]]; then
    echo "Error: Please provide a valid integer."
    exit 1
fi

# Use modulo operator to check if the number is even or odd
if [ $((NUMBER % 2)) -eq 0 ]; then
    echo "The number $NUMBER is even."
else
    echo "The number $NUMBER is odd."
fi
