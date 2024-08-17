import cv2
import numpy as np
import time
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)  # 0 is the id no. for the webcam
detector = HandDetector(maxHands=1)
offset = 20
imgSize = 350
#whenever we press 'S' it should save
folder= "C:\\Users\\lenovo\\OneDrive\\Desktop\\Python Folder\\HandGestureControl\\Data\\9"
counter=0


while True:
    success, img = cap.read()
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
            k = imgSize / imgCropShape[0] #if we stretch the value to 300 what is the value of width ...k is our constant
            wCal = int(k * imgCropShape[1])
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            imgResizeShape = imgResize.shape
            wGap = (imgSize - wCal) // 2
            imgWhite[:, wGap:wGap + imgResizeShape[1]] = imgResize
        elif aspectRatio < 1:
            # Width is greater than height
            k = imgSize / imgCropShape[1]
            hCal = int(k * imgCropShape[0])
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgResizeShape = imgResize.shape
            hGap = (imgSize - hCal) // 2
            imgWhite[hGap:hGap + imgResizeShape[0], :] = imgResize
        else:
            # Width and height are equal (aspect ratio == 1)
            imgResize = cv2.resize(imgCrop, (imgSize, imgSize))
            imgWhite[:imgSize, :imgSize] = imgResize

        cv2.imshow("ImageCrop", imgCrop)
        cv2.imshow("ImageWhite", imgWhite)

    cv2.imshow("Image", img)
    key=cv2.waitKey(1)  # 1 millisecond delay
    if key==ord('s') or key==ord('S'):
        counter+=1
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg',imgWhite)
        print(counter)