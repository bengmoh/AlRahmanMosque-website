from flask import Flask, render_template, request, redirect
from python_scripts.calculations import add_time, compare_iqama_times
import csv
import getpass
import os 
import pandas as pd
import platform


# Find username of the current user
user_name = getpass.getuser()

app = Flask(__name__)

@app.before_request
def redirect_non_www():
    if request.host.startswith('www.') or '127.0.0.1' in request.host:
        return None  # Don't redirect for localhost

    # Redirect to the www. subdomain
    new_url = request.url.replace('://', '://www.')
    return redirect(new_url, code=301)
if os.path.exists("data/prayer_times/today_prayer_times.csv"):
    df = pd.read_csv("data/prayer_times/today_prayer_times.csv")


os_type=platform.system()

if os_type == "Windows":
    base_dir = f'C:\\Users\\{user_name}'
elif os_type == "Linux":
    base_dir = f'/home/{user_name}'
elif os_type == "Darwin":  
    base_dir = f'/Users/{user_name}'
else:
    raise Exception("Unsupported OS")


def find_file(filename):
    for root, dirs, files in os.walk(base_dir):
        if filename in files:
            return os.path.join(root, filename)
    return None

files_path1 = find_file("today_prayer_times.csv")
files_path2 = find_file("programs.csv")
if not files_path1 or not files_path2:
    raise FileNotFoundError("Required CSV files not found.")

today = {}
with open(files_path1) as file:
    reader = csv.reader(file)
    for row in reader:
        prayer, athan, iqama = row
        today[prayer] = (athan, iqama)

programs = {}
with open(files_path2) as file:
    reader = csv.reader(file)
    for row in reader:
        title, description, time = row
        programs[title] = (description, time)
        
opening_time = add_time(today["Fajr"][1], -15, round_to_quarter=False)
closing_time = add_time(today["Isha"][1], 60, round_to_quarter=False)
time_changes = compare_iqama_times(
    "data/prayer_times/today_prayer_times.csv",
    "data/prayer_times/tomorrow_prayer_times.csv"
)
    
@app.route('/')
def index():
    return render_template("prayer_times.html", today=today,
                           opening_time=opening_time,
                           closing_time=closing_time,
                           time_changes=time_changes,
                           programs=programs)

@app.route('/prayer-times')
def prayer_times():
    return render_template("prayer_times.html", today=today)

@app.route('/donate')
def donate():
    return render_template("donate.html")

@app.route('/contact')
def contact():
    return render_template("contact.html",
                           opening_time=opening_time,
                           closing_time=closing_time)
app.run(debug=True)
