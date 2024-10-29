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
def home():
    return render_template("home.html", today=today)  
    