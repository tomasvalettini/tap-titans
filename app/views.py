from flask import render_template, flash, redirect
from app import app, models


@app.route('/')
@app.route('/index')
def index():
    heroes = models.Hero.query.all()
    upgrades = models.Upgrade.query.all()
    return render_template('index.html',
                           title='Tap Titans Upgrade',
                           heroes=heroes,
                           upgrades=upgrades)
