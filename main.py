from flask import Flask, render_template, request
from trainRoutes import fetch_train_times, to_crs
from flask_socketio import SocketIO

from flask import Flask, request, render_template
from chatgptai import getCities
app = Flask(__name__)
socketio = SocketIO(app) 

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

@app.route('/lisbon')
def libson():
    return render_template('lisbon.html')

@app.route('/cityIdeas')
def cityIdeas():
    
    return render_template('cityIdeas.html')

@app.route('/submitCity', methods=['POST'])
def submit():
    topic = request.form.get('topic')
    cityArray = getCities(topic=topic)
    city1 = cityArray[0]
    city2 = cityArray[1]
    city3 = cityArray[2]
    city4 = cityArray[3]
    city5 = cityArray[4]
    return render_template('cityIdeas.html', city1=city1, city2=city2, city3=city3, city4=city4, city5=city5)

if __name__ == '__main__':
    socketio.run(app)  

