# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 09:09:10 2015

@author: Ibrahim
"""

import cv2

face_csc = cv2.CascadeClassifier('haarcascade_smile.xml')
#cam = cv2.VideoCapture(1)

while(True):
    #tf, img = cam.read()    
    img = cv2.imread("smile.jpg")
       
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = face_csc.detectMultiScale(gray, 20.3, 4)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,0), 5)
        
    cv2.imshow('img', img)
    key = cv2.waitKey(1)
    if key == 27:
        break

#cam.release()
cv2.destroyAllWindows()