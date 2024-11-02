from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/routePlanner')
def routePlanner():
    return render_template('routePlanner.html')

@app.route('/team')
def theTeam():
    return render_template('TheTeam.html')