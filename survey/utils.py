import cv2
import mediapipe as mp
from keras.models import load_model
import numpy as np
def count_fingers(filename):
    mp_Hands = mp.solutions.hands
    hands = mp_Hands.Hands()
    mpDraw = mp.solutions.drawing_utils
    finger_Coord = [(8, 6), (12, 10), (16, 14), (20, 18)]
    thumb_Coord = (4,2)
    image = cv2.imread(filename)
    RGB_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(RGB_image)
    multiLandMarks = results.multi_hand_landmarks
    if multiLandMarks:
        handList = []
        for handLms in multiLandMarks:
            for idx, lm in enumerate(handLms.landmark):
   
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                handList.append((cx, cy))
    upCount = 0
    for coordinate in finger_Coord:
        if handList[coordinate[0]][1] < handList[coordinate[1]][1]:
            upCount += 1
    if handList[thumb_Coord[0]][0] > handList[thumb_Coord[1]][0]:
        upCount += 1
    return upCount

def emotion(filepath):
    class_labels={}
    class_labels = {0: 'Angry', 1: 'Disgust', 2: 'Fear', 3: 'Happy', 4: 'Neutral', 5: 'Sad', 6: 'Surprise'}
    image = cv2.imread(filepath)
    image = cv2.resize(image,(48,48))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
    
    
   
    image = np.reshape(image, (1, 48, 48))
    print(image.shape)
    
 
    # print(image.shape)
    model = load_model("survey\emotion-detector\model_v6_23.hdf5")
    predicted_class = class_labels[np.argmax(model.predict(image))]
    return predicted_class