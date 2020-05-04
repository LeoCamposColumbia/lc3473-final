# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
# THE THREE FOLLOWING ROUTES ARE FOR THE MAIN ASSIGNMENT (MAIN PAGE, ASSIGNMENT 
# PAGE, CLASSES PAGE)
@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/assignments")
def assignments():
    return render_template("assignments.html")

@app.route("/classes")
def classes():
    return render_template("classes.html")

# EVERYTHING THAT FOLLOWS IS TO RUN THE OPTIONAL/2nd HALF OF FINAL WHICH I DECIDED
# WOULD BE AN INTERACTIVE CHOOSE YOUR OWN ADVENTURE GAME

@app.route("/gamepage")
def game():
    return render_template("game.html")

@app.route("/gamepage/investigate")
def investigate():
    return render_template("investigate.html")

@app.route("/gamepage/bed")
def bed():
    return render_template("bed.html")

@app.route("/gamepage/bed/leave")
def leave():
    return render_template("leave.html")

@app.route("/gamepage/bed/window")
def dead():
    return render_template("bed.html")

@app.route("/win")
def win():
    return render_template("win.html")

#start the server
if __name__ == "__main__":
    app.run()