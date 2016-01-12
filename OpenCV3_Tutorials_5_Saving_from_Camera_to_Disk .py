import cv2
import numpy as np

#flags = [color for color in dir(cv2) if color.startswith('COLOR_')]
#print flags

cam = cv2.VideoCapture(1)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
vid = cv2.VideoWriter('output.avi', fourcc, 6, (640,480))

#count = 0
while(True):
    tf, frame = cam.read()
    #print tf
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #upper_red = np.array([130,255,255])
    #lower_red = np.array([110,100,100])
    #mask = cv2.inRange(frame, lower_red, upper_red)
    #frame = cv2.bitwise_and(frame,frame, mask=mask)
    #cv2.imwrite("frame{}.png".format(count), frame)
    #count +=1
    vid.write(frame)
    cv2.imshow('Single Frame', frame)
    key = cv2.waitKey(1)
    if key == 27: #esc key
        break
    elif key == ord('x'):
        print "You have pressed the letter X"

cam.release()
vid.release()
cv2.destroyAllWindows()


