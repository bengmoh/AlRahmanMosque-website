#!/bin/bash

cd /Users/macbook/projects/MosqueWebsite

# Activate virtual environment
source .venv/bin/activate

# Check if the virtual environment was activated successfully
if [[ $? -ne 0 ]]; then
  echo "Error activating virtual environment!" >> /tmp/cron_error.log
  exit 1
fi

# Print environment information for debugging
env > /tmp/cron_env.txt

# Run the scraper and check for errors
if ! python scraper.py > /tmp/cron_output.txt 2>&1; then
  echo "Error running scraper.py!" >> /tmp/cron_error.log
  exit 1
fi