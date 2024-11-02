from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/routePlanner')
def routePlanner():
    return render_template('routePlanner.html')