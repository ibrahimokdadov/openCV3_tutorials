import cv2
import numpy as np

img = cv2.imread('banana.jpg')
print img.shape

histogram = cv2.calcHist([img], [0], None, [16], [0,255])
#images, channels, mask, histSize, ranges
print histogram.shape
print "--"*10
print histogram
print "--"*10
print enumerate(histogram) #x,y
blank = np.zeros((255,256)) #black image aka blank 
for x,y in enumerate(histogram):
    #print x,y
    cv2.line(blank, (x,0), (x,y), (255,255,255))

cv2.imshow('histogram', blank)
cv2.waitKey(0)
cv2.destroyAllWindows()
    

