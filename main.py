from flask import Flask, render_template, request
from trainRoutes import fetch_train_times, to_crs
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)  # Initialize with app

@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/route_planner')
def route_planner():
    return render_template('routePlanner.html')

@socketio.on('get_train_times')
def get_train_times(station):
    print(f"station: {station}")
    CRSStation = to_crs(station['station'])
    train_times = fetch_train_times(CRSStation)
    print('sending train times')
    socketio.emit('train_times', train_times)

@app.route('/explore')
def explore():
    return render_template('explore.html')

@app.route('/team')
def theTeam():
    return render_template('TheTeam.html')

if __name__ == '__main__':
    socketio.run(app)  # Use socketio.run to start the app

