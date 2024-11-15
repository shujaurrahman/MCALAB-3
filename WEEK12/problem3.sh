#!/bin/bash

# Script to automate the creation of user accounts

# Check if the script is run as root
if [ "$(id -u)" -ne 0 ]; then
  echo "Please run this script as root."
  exit 1
fi

# Function to create a user
create_user() {
  local USERNAME=$1
  local PASSWORD=$2
  
  # Check if the user already exists
  if id "$USERNAME" &>/dev/null; then
    echo "User '$USERNAME' already exists."
    return
  fi

  # Create the user with a home directory
  useradd -m "$USERNAME"

  # Check if the user was created successfully
  if [ $? -eq 0 ]; then
    echo "User '$USERNAME' has been created."
    
    # Set the password if provided
    if [ -n "$PASSWORD" ]; then
      echo "$USERNAME:$PASSWORD" | chpasswd
      echo "Password for user '$USERNAME' has been set."
    else
      echo "No password provided. You may set it later using passwd $USERNAME."
    fi
  else
    echo "Failed to create user '$USERNAME'."
  fi
}

# Main script
echo "Enter the username for the new user:"
read -r USERNAME

echo "Enter the password for the new user (leave blank to skip):"
read -r -s PASSWORD

create_user "$USERNAME" "$PASSWORD"
