#!/bin/bash

cd /Users/macbook/projects/MosqueWebsite

# Copy tomorrow.csv to today.csv
if ! cp tomorrow.csv today.csv; then
  echo "Error copying tomorrow.csv to today.csv!" >> /tmp/cron_error.log
  exit 1
fi

# Commit changes
git add today.csv

if ! git commit --amend --no-edit; then
  echo "Error committing changes!" >> /tmp/cron_error.log
  exit 1
fi

# Pull latest changes from remote (without opening an editor)
if ! git pull --no-edit; then
  echo "Error pulling changes!" >> /tmp/cron_error.log
  exit 1
fi

# Force push the amended commit 
if ! git push -f; then
  echo "Error pushing changes!" >> /tmp/cron_error.log
  exit 1
fi