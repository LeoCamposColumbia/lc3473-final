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
    '''Renders home page'''
    return render_template("home.html")

@app.route("/assignments")
def assignments():
    '''Renders assignments page'''
    return render_template("assignments.html")

@app.route("/classes")
def classes():
    '''Renders classes page'''
    return render_template("classes.html")

# EVERYTHING THAT FOLLOWS IS TO RUN THE OPTIONAL/2nd HALF OF FINAL WHICH I DECIDED
# WOULD BE AN INTERACTIVE CHOOSE YOUR OWN ADVENTURE GAME

@app.route("/gamemenu")
def gamemenu():
    '''Renders startup game menu'''
    return render_template("gamemenu.html")

@app.route("/gamepage")
def game():
    '''Renders first game page'''
    return render_template("game.html")

@app.route("/gamepage/bed")
def bed():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("bed.html")

@app.route("/gamepage/bed/leave")
def leave():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("leave.html")

@app.route("/gamepage/bed/leave/stab")
def stab():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("stab.html")

@app.route("/gamepage/bed/leave/stab/downstairs")
def downstairs():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("downstairs.html")

@app.route("/gamepage/bed/leave/stab/downstairs/stealth")
def stealth():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("stealth.html")

@app.route("/gamepage/bed/leave/run")
def run():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("run.html")

@app.route("/gamepage/bed/leave/run/still")
def still():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("still.html")

@app.route("/gamepage/bed/leave/run/still/hide")
def hide():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("hide.html")

@app.route("/gamepage/bed/leave/run/still/fight")
def fight():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("fight.html")

@app.route("/gamepage/bed/leave/run/still/fight/break")
def breaks():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("break.html")

@app.route("/gamepage/bed/leave/run/still/fight/unlock")
def unlock():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("unlock.html")

@app.route("/gamepage/bed/leave/run/door")
def door():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("door.html")

@app.route("/gamepage/bed/window")
def window():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("window.html")

@app.route("/gamepage/investigate")
def investigate():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("investigate.html")

@app.route("/gamepage/investigate/swing")
def swing():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("swing.html")

@app.route("/gamepage/investigate/swing/basement")
def basement():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("basement.html")

@app.route("/gamepage/investigate/swing/basement/stealthy")
def stealthy():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("stealthy.html")

@app.route("/gamepage/investigate/runningman")
def runningman():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("runningman.html")

@app.route("/gamepage/earlydeparture")
def earlydeparture():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("earlydeparture.html")

@app.route("/gamepage/runenddeath")
def runenddeath():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("runenddeath.html")

@app.route("/part2")
def second():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("part2.html")

@app.route("/part2/kid")
def kid():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("kid.html")

@app.route("/part2/kid/you")
def you():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("you.html")

@app.route("/part2/kid/both")
def both():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("both.html")

@app.route("/part2/drive")
def drive():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("drive.html")

@app.route("/part2/drive/embrace")
def embrace():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("embrace.html")

@app.route("/part2/drive/nocando")
def nope():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("nocando.html")

@app.route("/part2b")
def bad():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("part2b.html")

@app.route("/part2b/pickup")
def pickup():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("pickup.html")

@app.route("/part2b/pickup/me")
def me():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("me.html")

@app.route("/part2b/pickup/me/towards")
def towards():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("towards.html")

@app.route("/part2b/pickup/me/away")
def away():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("away.html")

@app.route("/part2b/pickup/us")
def us():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("us.html")

@app.route("/part2b/pickup/us/frontdoor")
def frontdoor():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("frontdoor.html")

@app.route("/part2b/pickup/us/backdoor")
def backdoor():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("backdoor.html")

@app.route("/part2b/go")
def go():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("go.html")

@app.route("/part2b/go/together")
def together():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("together.html")

@app.route("/part2b/go/noway")
def noway():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("noway.html")

@app.route("/news1")
def news1():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("news1.html")

@app.route("/news2")
def news2():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("news2.html")

@app.route("/news3")
def news3():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("news3.html")

@app.route("/news4")
def news4():
    '''Renders one of many scenarios based on player's choices'''
    return render_template("news4.html")

#start the server
if __name__ == "__main__":
    app.run()