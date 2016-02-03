import cv2

names = [name for name in dir(cv2) if name.startswith('CV_')]
print names
