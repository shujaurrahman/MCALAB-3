#!/bin/bash

# Disk usage monitor script
# Usage: ./disk_monitor.sh [threshold_percentage]

# Set threshold percentage (default to 80 if not provided)
THRESHOLD=${1:-80}

# Define the directory or mount point to monitor (e.g., root "/")
MOUNT_POINT="/"

# Check disk usage
USAGE=$(df -h "$MOUNT_POINT" | awk 'NR==2 {print $5}' | sed 's/%//')

# Check if disk usage exceeds threshold
if [ "$USAGE" -ge "$THRESHOLD" ]; then
  echo "Alert: Disk usage is at ${USAGE}% on ${MOUNT_POINT} (Threshold: ${THRESHOLD}%)"
  
  # Send an alert (e.g., via email)
  # mail -s "Disk Usage Alert: ${USAGE}% used" your_email@example.com <<< "Disk usage on $MOUNT_POINT has reached ${USAGE}%."
else
  echo "Disk usage is under control: ${USAGE}% on ${MOUNT_POINT}."
fi
