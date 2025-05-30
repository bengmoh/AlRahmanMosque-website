from flask import Flask, render_template, request, redirect
from python_scripts.calculations import add_time, compare_iqama_times
import csv

app = Flask(__name__)

# Remove comment if redirecting to a domain starting with www.
@app.before_request
def redirect_non_www():
    if request.host.startswith('www.'):
        return None  # Continue with the request if it's already on www.

    # Redirect to the www. subdomain
    new_url = request.url.replace('://', '://www.')
    return redirect(new_url, code=301)

today = {}
with open("data/prayer_times/today_prayer_times.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        prayer, athan, iqama = row
        today[prayer] = (athan, iqama)

programs = {}
with open("data/programs.csv") as file:
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