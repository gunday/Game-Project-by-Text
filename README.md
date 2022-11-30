# Playing With Digital Book Project
Python Flask web application for the Fighting Fantasy book series.


Based on Fighing Fantasy Scenario and Game Books!

No it's not an attempt to remove fantasy from the world, in fact I would like to see more in the world.

Fighting Fantasy is actually a book series (I believe there are 53 of them) of choose your own adventure gamebooks. This means not only are they choose your own adventure, but they are RPG/Table top games requiring dice to be rolled for battles and other situations.

This Python Flask web app is designed to accept your characters stats and those of any enemy encountered and complete the following:

    Roll your dice
    Roll the enemy dice
    Calculate who won the round
    Ask if you would like to use luck to modify the outcome of the round
    Calculate damage agains you or the enemy
    Keep track of health until you or the enemy is dead

# How to use it

The current python logic is not setup in the Flask app so if you would like to use the encounter calculator at this time please download and then go to FightingFantasy/
From this directory you can run the functions.py file:
python functions.py

This will allow a terminal run of the encounter calculator.


# Running the Flask App

Entering the FightingFantasy folder and using the following command will start the flask app:

python run.py

Access the page at http://127.0.0.1:5000 (feel free to change this in the code if you would like) will bring up the home page of the web app.


# Soon!

This is a side project that I'm just sorta futzing around with so I don't have a set release schedule. Sorry for that.

But please know that I will be moving the logic to be accessed by Flask, setting up a simple db and using Flask-WTF for some input along with other items.