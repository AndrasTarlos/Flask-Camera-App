import io

import numpy
from PIL import Image

'''
import cv2

# Gets all the trained values
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Saves an image in a var
# img = cv2.imread('ghwalin.jpeg')
webcam = cv2.VideoCapture(0)


while True:
    successful_frame_read, frame = webcam.read()
    # Convert to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect face
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    if len(face_coordinates) > 1:
        face_coordinates = face_coordinates[:len(face_coordinates) - 1]

    # Draw rectangles around the faces
    for (x, y, w, h) in face_coordinates:
        # (x, y, w, h) = face_coordinates[1]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Face detector", frame)
    # Waits until you close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


webcam.release()
cv2.destroyAllWindows()

print("Code completed")


'''
import cv2


def create_coordinates(byte_data):
    pil_img = Image.open(io.BytesIO(byte_data)).convert("RGB")
    ocv_image = numpy.array(pil_img)
    ocv_image = ocv_image[:, :, ::-1].copy()
    trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    grayscaled_img = cv2.cvtColor(ocv_image, cv2.COLOR_BGR2GRAY)
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    return face_coordinates


def show(img):
    cv2.imshow("output", img)
    cv2.waitKey(0)

