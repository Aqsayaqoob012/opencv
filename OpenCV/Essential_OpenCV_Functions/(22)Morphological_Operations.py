import cv2
import numpy as np
# Load grayscale image
image = cv2.imread('01.jpg' , 0)

# Define Kernel
kernal = np.ones((5,5), np.uint8 )

# Apply Erosion
img_erosion = cv2.erode(image , kernal , iterations=1)

# Apply Dilation
img_dilation = cv2.dilate(image , kernal , iterations=1)

cv2.imshow('Original Image ' , image)
cv2.imshow('Erosion ' , img_erosion)
cv2.imshow('Dilation' , img_dilation)

if cv2.waitKey(0) & 0xff == ord('q'):
    cv2.destroyAllWindows()
