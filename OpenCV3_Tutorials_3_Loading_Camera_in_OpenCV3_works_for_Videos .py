import cv2
import numpy as np

cam = cv2.VideoCapture(1)

while(True):
    tf, frame = cam.read()
    #print tf
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    upper_red = np.array([130,255,255])
    lower_red = np.array([110,100,100])
    mask = cv2.inRange(frame, lower_red, upper_red)
    frame = cv2.bitwise_and(frame,frame, mask=mask)    
    cv2.imshow('Single Frame', frame)
    key = cv2.waitKey(1)
    if key == 27: #esc key
        break
    elif key == ord('x'):
        print "You have pressed the letter X"

cam.release()
cv2.destroyAllWindows()


