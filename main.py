from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/routePlanner')
def routePlanner():
    return render_template('routePlanner.html')

@app.route('/explore')
def explore():
    return render_template('explore.html')


@app.route('/team')
def theTeam():
    return render_template('TheTeam.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/paris')
def paris():
    return render_template('paris.html')

@app.route('/berlin')
def berlin():
    return render_template('berlin.html')

@app.route('/london')
def london():
    return render_template('london.html')