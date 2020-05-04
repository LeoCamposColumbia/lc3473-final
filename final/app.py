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

@app.route("/gamepage/bed")
def bed():
    return render_template("bed.html")

@app.route("/gamepage/bed/leave")
def leave():
    return render_template("leave.html")

@app.route("/gamepage/bed/leave/stab")
def stab():
    return render_template("stab.html")

@app.route("/gamepage/bed/leave/stab/downstairs")
def downstairs():
    return render_template("downstairs.html")

@app.route("/gamepage/bed/leave/stab/downstairs/stealth")
def stealth():
    return render_template("stealth.html")

@app.route("/gamepage/bed/leave/run")
def run():
    return render_template("run.html")

@app.route("/gamepage/bed/leave/run/still")
def still():
    return render_template("still.html")

@app.route("/gamepage/bed/leave/run/still/hide")
def hide():
    return render_template("hide.html")

@app.route("/gamepage/bed/leave/run/still/fight")
def fight():
    return render_template("fight.html")

@app.route("/gamepage/bed/leave/run/still/fight/break")
def breaks():
    return render_template("break.html")

@app.route("/gamepage/bed/leave/run/still/fight/unlock")
def unlock():
    return render_template("unlock.html")

@app.route("/gamepage/bed/leave/run/door")
def door():
    return render_template("door.html")

@app.route("/gamepage/bed/window")
def window():
    return render_template("window.html")

@app.route("/gamepage/investigate")
def investigate():
    return render_template("investigate.html")

@app.route("/gamepage/investigate/swing")
def swing():
    return render_template("swing.html")

@app.route("/gamepage/investigate/swing/basement")
def basement():
    return render_template("basement.html")

@app.route("/gamepage/investigate/swing/basement/stealthy")
def stealthy():
    return render_template("stealthy.html")

@app.route("/gamepage/investigate/runningman")
def runningman():
    return render_template("runningman.html")

@app.route("/gamepage/earlydeparture")
def earlydeparture():
    return render_template("earlydeparture.html")

@app.route("/gamepage/runenddeath")
def runenddeath():
    return render_template("runenddeath.html")

#start the server
if __name__ == "__main__":
    app.run()