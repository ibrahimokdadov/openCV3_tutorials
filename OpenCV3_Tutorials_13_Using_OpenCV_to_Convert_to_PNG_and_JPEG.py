import cv2


img = cv2.imread('pond.jpg')
print "converting image..."
cv2.imwrite('pond_converted.png', img, [cv2.IMWRITE_JPEG_QUALITY, 10])
print "finished...."
