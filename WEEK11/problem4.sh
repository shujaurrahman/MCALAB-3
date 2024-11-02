#!/bin/bash

# Function to greet the user
greet_user() {
    local name=$1  # Get the first argument passed to the function
    echo "Hello, $name! Welcome to the shell scripting world!"
}

# Check if a name is provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <name>"
    exit 1
fi

# Call the greet_user function with the provided argument
greet_user "$1"
