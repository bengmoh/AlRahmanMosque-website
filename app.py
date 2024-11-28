from flask import Flask, render_template, request, redirect
from python_scripts.calculations import add_time
import csv

app = Flask(__name__)

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
    opening_time = add_time(today["Fajr"][1], -15, round_to_quarter=False)
    closing_time = add_time(today["Isha"][1], 60, round_to_quarter=False)
    
@app.route('/')
def index():
    return render_template("prayer_times.html", today=today,
                           opening_time=opening_time,
                           closing_time=closing_time)

@app.route('/prayer-times')
def prayer_times():
    return render_template("prayer_times.html", today=today)

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/donate')
def donate():
    return render_template("donate.html")