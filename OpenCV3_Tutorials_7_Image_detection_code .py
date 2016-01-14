# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 09:09:10 2015

@author: Ibrahim
"""

import cv2

img = cv2.imread("me2.jpg")
face_csc = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_csc.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,0), 5)
    
cv2.imshow('img', img)
cv2.waitKey(0)