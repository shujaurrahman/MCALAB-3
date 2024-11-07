#!/bin/bash

# FILENAME="ex.txt"

if [ $# -eq 0 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

FILENAME=$1


if [ -e "$FILENAME" ]; then
    echo "The file '$FILENAME' exists."
else
    echo "The file '$FILENAME' does not exist."
fi

