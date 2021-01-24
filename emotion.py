import os
import cv2
import numpy as np
import tensorflow as tf

# Load model
model = tf.keras.models.model_from_json(open("model.json", "r").read())

# Load weights
model.load_weights("model.h5")

face_haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                          "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

time_counter = 0
time_interval = 50

while True:
    ret, test_image = cap.read()
    if (time_counter != time_interval) or not ret:
        time_counter += 1
        continue
    else:
        time_counter = 0

    gray_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)
    faces_detected = face_haar_cascade.detectMultiScale(gray_image, 1.32, 5)

    for (x, y, w, h) in faces_detected:
        cv2.rectangle(test_image, (x, y), (x+w, y+h), (255, 0, 0), thickness=7)
        roi_gray = gray_image[y:y+w, x:x+h]
        roi_gray = cv2.resize(roi_gray, (48, 48))
        image_pixels = tf.keras.preprocessing.image.img_to_array(roi_gray)
        image_pixels = np.expand_dims(image_pixels, axis=0)
        image_pixels /= 255.0
        predictions = model.predict(image_pixels)
        max_index = np.argmax(predictions[0])
        emotions = ('angry', 'disgust', 'fear', 'happy',
                    'sad', 'surprise', 'neutral')
        predicted_emotion = emotions[max_index]
        cv2.putText(test_image, predicted_emotion, (int(x), int(y)),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    resized_image = cv2.resize(test_image, (1000, 700))
    cv2.imshow('Facial emotion analysis ', resized_image)

    if cv2.waitKey(10) == ord('q'):  # wait until 'q' key is pressed
        break

cap.release()
cv2.destroyAllWindows
