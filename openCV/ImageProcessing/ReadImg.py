#python --version

#to install openCV
#pip install opencv-python


#to check openCV version
import cv2
print(cv2.__version__)


#import the library
import cv2 as cv


#read the image from the stored location
img=cv.imread('ComputerVision\openCV\ImageProcessing\dog1.jpeg')

#display the images in a new window
cv.imshow("Image", img)

cv.waitKey(0)

