from flask import Flask, render_template
import csv

app = Flask(__name__)

today = {}
with open("today.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        prayer, athan, iqama = row
        today[prayer] = (athan, iqama)
    
@app.route('/')
def index():
    return render_template("prayer_times.html", today=today)

@app.route('/prayer-times')
def prayer_times():
    return render_template("prayer_times.html", today=today)

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/donate')
def donate():
    return render_template("donate.html")