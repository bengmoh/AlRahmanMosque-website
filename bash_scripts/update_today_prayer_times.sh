#!/bin/bash

cd /Users/macbook/projects/MosqueWebsite

# Pull latest changes from remote (without opening an editor)
if ! git pull --no-edit; then
  echo "Error pulling changes!" >> /tmp/cron_error.log
  exit 1
fi

# Copy tomorrow.csv to today.csv
if ! cp data/prayer_times/tomorrow_prayer_times.csv data/prayer_times/today_prayer_times.csv; then
  echo "Error copying tomorrow_prayer_times to today_prayer_times!" >> /tmp/cron_error.log
  exit 1
fi

# Commit changes
git add data/prayer_times/today_prayer_times.csv

if ! git commit --amend --no-edit; then
  echo "Error committing changes!" >> /tmp/cron_error.log
  exit 1
fi

# Force push the amended commit 
if ! git push -f; then
  echo "Error pushing changes!" >> /tmp/cron_error.log
  exit 1
fi