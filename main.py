import base64
import os
import re
#import cv2
import numpy
from PIL import Image

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

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

    print("Hi Moustafa")
    '''
    pil_img = Image.open(io.BytesIO(byte_data)).convert("RGB")
    ocv_image = numpy.array(pil_img)
    ocv_image = ocv_image[:, :, ::-1].copy()
    trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    grayscaled_img = cv2.cvtColor(ocv_image, cv2.COLOR_BGR2GRAY)
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    '''


@socketio.on('message')
def send_face_coordinates(coordinates):
    emit("receive_face_coordinates", coordinates)

    '''
    (x, y, w, h) = create_coordinates(img)
    emit("face_coordinates", {"x": x, "y": y, "w": w, "h": h})
    '''


if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 8080)), host='0.0.0.0', debug=True)
    #socketio.run(app, port=int(os.environ.get("PORT", 3000)), host='0.0.0.0', debug=True)
