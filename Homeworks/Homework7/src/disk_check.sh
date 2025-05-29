#!/bin/bash

THRESHOLD=$1
LOG_FILE="/var/log/disk.log"

# Check if threshold is provided and is a number
if ! [[ "$THRESHOLD" =~ ^[0-9]+$ ]]; then
  echo "Usage: $0 <threshold_percentage>"
  exit 1
fi

# Get disk usage as integer
USAGE=$(df / | awk 'NR==2 {gsub("%", ""); print $5}')
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

if [ "$USAGE" -gt "$THRESHOLD" ]; then
  echo "$TIMESTAMP WARNING: / disk usage is at ${USAGE}%, exceeds threshold of ${THRESHOLD}%" >> "$LOG_FILE"
fi

