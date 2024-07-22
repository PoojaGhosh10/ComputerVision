#python --version

#to install openCV
#pip install opencv-python


#to check openCV version
import cv2
print(cv2.__version__)


#import the library
import cv2 as cv


#read the image from the stored location  -path, flag(the way in which it should be read)
#return a NumPy array if the image is loaded successfully.
img=cv.imread('ComputerVision\openCV\ImageProcessing\dog1.jpeg', cv.IMREAD_GRAYSCALE)#IMREAD_COLOR, IMREAD_GRAYSCALE, IMREAD_UNCHANGED

#display the images in a new GUI window---windowname , image variable
cv.imshow("Image", img)#return nothing

#to save the image in a location
path=r'C:\\Users\\lenovo\\OneDrive\\Desktop\\Python Folder\\ComputerVision\\openCV\\ImageProcessing\\dog1_gr1_sc.jpg'
#it returns boolean if image is saved
print(cv.imwrite(path, img))

#To hold the window on screen , first aprameter is for holding screen for milliseconds. 0 for holding the screen untill the user closees it.
cv.waitKey(0)

#to destroy the windows from the memory after displaying 
#cv.destroyAllWindows()



