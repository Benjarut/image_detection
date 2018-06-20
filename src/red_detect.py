#!/usr/bin/env python

import numpy as np
import argparse
import cv2

if __name__ == '__main__':

	# construct the argument parse and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--image", help = "path to the image")
	args = vars(ap.parse_args())
	print("Hello World")
	# load the image
	img = cv2.imread(args["image"])
	cv2.imshow("Input Image",img)

	#convert frame RGB to HSV
	hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

	#defining the range of the red color
	red_lower=np.array([0,100,140],np.uint8)
	red_upper=np.array([5,255,255],np.uint8)

	#finding the range of red color in image
	red=cv2.inRange(hsv, red_lower, red_upper)
	cv2.imshow("Red",red)

	#Morphological transformation, Dilation
	kernal = np.ones((5, 5), "uint8")

	red=cv2.dilate(red, kernal)
	res=cv2.bitwise_and(img, img, mask = red)

	#Tracking the Red Color
	(_,contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	if len(contours) != 0:
		#find the biggest area
		c = max(contours, key = cv2.contourArea)
		print(c)
		x,y,w,h = cv2.boundingRect(c)
		img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		cv2.putText(img,"RED color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))

	cv2.imshow("Color Tracking",img)
	cv2.imwrite('/home/omega/Color4.png',img)


