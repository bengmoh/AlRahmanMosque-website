#!/Users/macbook/projects/MosqueWebsite/.venv/bin/python3

import requests
from bs4 import BeautifulSoup
import csv
from iqama import *

def main(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes

    soup = BeautifulSoup(response.content, "html.parser")

    # Find the athan times table
    athan_times_table = soup.find("table", class_="prayertimerange")

    # Extract athan times for tomorrow
    athan_times = {}
    if athan_times_table:
        row = athan_times_table.find("tbody").find_all("tr")[1]  # Get the 2nd row
        columns = row.find_all("td")
        athan_times = {
            "Fajr": columns[1].text.strip(),
            "Dhuhr": columns[3].text.strip(),
            "Asr": columns[4].text.strip(),
            "Maghrib": columns[5].text.strip(),
            "Isha": columns[6].text.strip()
        }

    with open("/Users/macbook/projects/MosqueWebsite/tomorrow.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for prayer, athan in athan_times.items():
            writer.writerow([prayer, athan, iqama(prayer, athan)])

if __name__=="__main__":
    url = "https://timesprayer.com/en/prayer-times-in-toronto-m2j0t1.html"
    try:
        main(url)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
