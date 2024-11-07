#!/bin/bash

cd /Users/macbook/projects/MosqueWebsite

# Pull latest changes from remote
git pull origin main 

# Copy tomorrow.csv to today.csv
if ! cp tomorrow.csv today.csv; then
  echo "Error copying tomorrow.csv to today.csv!" >> /tmp/cron_error.log
  exit 1
fi

# Commit and push changes
git add today.csv

if ! git commit --amend --no-edit; then
  echo "Error committing changes!" >> /tmp/cron_error.log
  exit 1
fi

if ! git push; then
  echo "Error pushing changes!" >> /tmp/cron_error.log
  exit 1
fi