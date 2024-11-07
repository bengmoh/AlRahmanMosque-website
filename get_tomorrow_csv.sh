#!/bin/bash

cd /Users/macbook/projects/MosqueWebsite

# Pull latest changes from remote (without opening an editor)
if ! git pull --no-edit; then
  echo "Error pulling changes!" >> /tmp/cron_error.log
  exit 1
fi

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

# Commit changes
git add tomorrow.csv

if ! git commit --amend --no-edit; then
  echo "Error committing changes!" >> /tmp/cron_error.log
  exit 1
fi

# Force push the amended commit 
if ! git push -f; then
  echo "Error pushing changes!" >> /tmp/cron_error.log
  exit 1
fi