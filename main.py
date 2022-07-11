import base64
import re

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from face_detector import *

app = Flask(__name__)
app.config['MASTER_KEY'] = 'admin'
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")


'''
@socketio.on("my event")
def test_message(message):
    emit("my response", {"data": message["data"]})

@socketio.on("my broadcast event")
def test_message(message):
    emit("my respones", {"data": message["data"]}, broadcast=True)
'''


@socketio.on("connect")
def connect():
    print("User connected")


@socketio.on("receive_frame")
def get_face_coordinates(base64_data):
    image_data = re.sub('^data:image/.+;base64,', '', base64_data)
    byte_data = base64.urlsafe_b64decode(image_data)
    face_coordinates = create_coordinates(byte_data)
    send_face_coordinates(face_coordinates)


@socketio.on('message')
def send_face_coordinates(coordinates):
    emit("receive_face_coordinates", coordinates)

    '''
    (x, y, w, h) = create_coordinates(img)
    emit("face_coordinates", {"x": x, "y": y, "w": w, "h": h})
    '''


if __name__ == "__main__":
    socketio.run(app, debug=False, host="0.0.0.0")
