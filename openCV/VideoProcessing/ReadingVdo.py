import cv2 as cv

#read the video from the storage
capture1= cv.VideoCapture("ComputerVision\openCV\VideoProcessing\cute_dog_vd.mp4")

#read the video from livecam 0 for live cam and path for stored video
capture2= cv.VideoCapture(0)

#to check if it is successfully opened or not. It returns the Boolean value.
print(capture1.isOpened())
print(capture2.isOpened())

#release the video after processing
capture1.release()
capture2.release()
