import cv2
import numpy as np
import tensorflow as tf
import keras
import time
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
cap = cv2.VideoCapture(0)  # 0 is the id no. for the webcam
detector = HandDetector(maxHands=1)
path="C:\\Users\\lenovo\\OneDrive\\Desktop\\Python Folder\\HandGestureControl\\Model\\keras_model.h5"
labelOutput="C:\\Users\\lenovo\\OneDrive\\Desktop\Python Folder\\HandGestureControl\\Model\\labels.txt"


classifier=Classifier(path, labelOutput)

offset = 20
imgSize = 350

counter=0
labels=["A", "B","C", "D", "E", "F","G", "H", "I", "J","K", "L","M", "N","O", "P","Q", "R","S", "T","U", "V","W", "X","X", "Y","Z", "1","2", "3","4", "5","6", "7","8", "9","0"]

while True:
    success, img = cap.read()
    imgOutput= img.copy()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255

        # Ensure crop coordinates are within the image dimensions
        y1 = max(0, y - offset)
        y2 = min(img.shape[0], y + h + offset)
        x1 = max(0, x - offset)
        x2 = min(img.shape[1], x + w + offset)

        imgCrop = img[y1:y2, x1:x2]
        imgCropShape = imgCrop.shape

        # Determine whether to scale by width or height
        aspectRatio = imgCropShape[0] / imgCropShape[1]  # Height / Width

        if aspectRatio > 1:
            # Height is greater than width
            k = imgSize / imgCropShape[0] #if we stretch the value to 300 what is the value of width ...k is the constant
            wCal = int(k * imgCropShape[1])
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            imgResizeShape = imgResize.shape
            wGap = (imgSize - wCal) // 2
            imgWhite[:, wGap:wGap + imgResizeShape[1]] = imgResize
            prediction, index=classifier.getPrediction(imgWhite, draw=False)
            print(prediction, index)

        elif aspectRatio < 1:
            # Width is greater than height
            k = imgSize / imgCropShape[1]
            hCal = int(k * imgCropShape[0])
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgResizeShape = imgResize.shape
            hGap = (imgSize - hCal) // 2
            imgWhite[hGap:hGap + imgResizeShape[0], :] = imgResize
            prediction, index=classifier.getPrediction(imgWhite, draw=False)
            print(prediction, index)
        else:
            # Width and height are equal (aspect ratio == 1)
            imgResize = cv2.resize(imgCrop, (imgSize, imgSize))
            imgWhite[:imgSize, :imgSize] = imgResize
            prediction, index=classifier.getPrediction(imgWhite)
            print(prediction, index)

        cv2.rectangle(imgOutput, (x-offset, y-offset-50), (x-offset+90, y-offset-50+50), (255,0,255),cv2.FILLED)
        cv2.putText(imgOutput, labels[index],(x, y-27), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.7,(255,255,255),2)
        cv2.rectangle(imgOutput, (x-offset, y-offset), (x+w+offset, y+h+offset), (255,0,255),4)
        cv2.imshow("ImageCrop", imgCrop)
        cv2.imshow("ImageWhite", imgWhite)

    cv2.imshow("Image", imgOutput)
    cv2.waitKey(1000)  # 1 millisecond delay
    