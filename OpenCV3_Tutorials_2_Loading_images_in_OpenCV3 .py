import cv2

img = cv2.imread('b.PNG', cv2.IMREAD_COLOR)
print img
if img is None:
    print "Object does not exist"
else:
    cv2.imshow('firstImg', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
