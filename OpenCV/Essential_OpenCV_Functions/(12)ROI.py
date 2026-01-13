# Extracting the Region of Interest (ROI) 
import cv2 
image = cv2.imread('1.jpg')

roi = image [25:100 , 150:250]
cv2.imshow('ROI' , roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
OpenCV image slicing NumPy ke rules follow karti hai:
image[y1 : y2, x1 : x2]

y1 = 25  (top)
y2 = 100   (bottom)

x1 = 150   (left)
x2 = 250   (right)
'''