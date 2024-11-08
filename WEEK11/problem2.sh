#!/bin/bash

# Function to calculate factorial
factorial() {
    local num=$1
    local result=1

    # Loop to calculate factorial
    for (( i=1; i<=num; i++ )); do
        result=$((result * i))
    done

    echo "The factorial of $num is $result."
}

# Check if a number is provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <number>"
    exit 1
fi

# Call the factorial function with the provided argument
factorial $1
