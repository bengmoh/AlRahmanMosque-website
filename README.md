# Al-Rahman Mosque Website

This project is a Flask-based website for Al-Rahman Mosque, designed to provide the community with accurate prayer times, announcements, and donation options. The website was deployed on DigitalOcean and used GitHub Actions to automate daily prayer time updates.

## Features

- **Automated Prayer Times**: Fetches daily prayer times from a reputable source and calculates Iqama times.
- **Time Change Alerts**: Detects and displays changes in prayer times for the following day.
- **Donation Options**: Supports e-transfer and online payments (coming soon).
- **Announcements**: Displays important announcements, Jumu'ah times, and upcoming programs.
- **Responsive Design**: Ensures the website is accessible on all devices.

## How It Works

1. **Prayer Times Scraping**: The `scraper.py` script fetches prayer times from [TimesPrayer](https://timesprayer.com) and calculates Iqama times using the `calculations.py` script.
2. **Daily Updates**: GitHub Actions triggers a daily workflow to update prayer times and detect any changes.
3. **Website Deployment**: The Flask app is deployed on DigitalOcean using Gunicorn and Nginx.

## Files Overview

- `scraper.py`: Fetches and processes prayer times.
- `calculations.py`: Contains functions to calculate Iqama times and detect changes.
- `gunicorn_config.py`: Configuration for Gunicorn server.
- `templates/`: HTML templates for the website.
- `static/`: CSS and JavaScript files for styling and interactivity.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/bengmoh/AlRahmanMosque-website.git

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the Flask app:
   ```bash
   flask run

Set up GitHub Actions for daily updates.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- TimesPrayer for providing prayer times.
- DigitalOcean AppPlatform service for hosting.
- GitHub Actions for prayer times data automation.
