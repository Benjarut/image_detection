#!/usr/bin/env python

# importing modules
import numpy as np
import argparse
import cv2


if __name__ == '__main__':
	# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	print("Hello")

	# construct the argument parse and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--image", help = "path to the image")
	args = vars(ap.parse_args())

	# load the image
	img = cv2.imread(args["image"])
	cv2.imshow("Input Image",img)

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		roi_gray = gray[y:y+h, x:x+w]

	cv2.imshow("Face detect",img)
	cv2.imwrite('./face.png',img)

	if cv2.waitKey(0) & 0xFF:
		cv2.destroyAllWindows()
