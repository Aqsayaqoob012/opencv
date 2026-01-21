# Image translation ka matlab hai image ko horizontal ya vertical direction me shift karna.
# OpenCV me `cv2.warpAffine()` aur translation matrix use hota hai.
# Translation matrix format: [[1, 0, tx], [0, 1, ty]] 
# tx → horizontal shift, ty → vertical shift

import cv2
import numpy as np

# Step 1: Load Image
image = cv2.imread('car1.jpg')

# Step 2: Get Image Dimensions
height, width = image.shape[:2]

# Step 3: Define Translation Distances
# x-direction = width/4, y-direction = height/4
tx = width / 4
ty = height / 4

# Step 4: Create Translation Matrix
# [1 0 tx]
# [0 1 ty]
T = np.float32([[1, 0, tx],
                [0, 1, ty]])

# Step 5: Apply warpAffine for Translation
translated_image = cv2.warpAffine(image, T, (width, height))


cv2.imshow('originl Image' , image )
cv2.imshow('translated Image' , translated_image )

cv2.waitKey(0)
cv2.destroyAllWindows()