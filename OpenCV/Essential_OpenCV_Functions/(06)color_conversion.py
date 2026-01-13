# Color conversion ka matlab hai image ko ek color space se doosre me convert karna.
# OpenCV me `cv2.cvtColor()` use hota hai.
# Example color spaces:
#   cv2.COLOR_BGR2GRAY  → BGR (original) se Grayscale
#   cv2.COLOR_BGR2RGB   → BGR se RGB
#   cv2.COLOR_BGR2HSV   → BGR se HSV (Hue, Saturation, Value)

import cv2
image = cv2.imread('1.jpg')

# Color image ko black & white me convert karta hai 
grey = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

# BGR → RGB
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

cv2.imshow('Original Image' , image)
cv2.imshow('Grey' , grey)
cv2.imshow('RGB' , rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
