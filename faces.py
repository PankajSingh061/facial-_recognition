import cv2
import pickle
import numpy as np
import os

video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

faces_data = []
i = 0

name = input("Enter Your Name: ")

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        crop_img = frame[y:y + h, x:x + w, :]
        resized_img = cv2.resize(crop_img, (50, 50))
        if len(faces_data) <= 100 and i % 10 == 0:
            faces_data.append(resized_img)
        i = i + 1
        cv2.putText(frame, str(len(faces_data)), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 255), 1)
    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1)
    if k == ord('q') or len(faces_data) == 100:
        break
video.release()
cv2.destroyAllWindows()

faces_data = np.asarray(faces_data)
faces_data = faces_data.reshape(100, -1)

# Load existing data or create a new file
if 'faces_data.pkl' not in os.listdir('data/'):
    data_array = np.empty((0, faces_data.shape[1]), dtype=np.uint8)
else:
    with open('data/faces_data.pkl', 'rb') as f:
        data_array = pickle.load(f)

# Append new data to the existing data
data_array = np.vstack((data_array, faces_data))

# Save the combined data back to the file
with open('data/faces_data.pkl', 'wb') as f:
    pickle.dump(data_array, f)

# Store the corresponding names
if 'names.pkl' not in os.listdir('data/'):
    names = [name] * 100
else:
    with open('data/names.pkl', 'rb') as f:
        names = pickle.load(f)
    names = names + [name] * 100

# Save the names
with open('data/names.pkl', 'wb') as f:
    pickle.dump(names, f)
