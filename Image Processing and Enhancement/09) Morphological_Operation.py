# Morphological operations image me shapes aur structures ko enhance ya modify karne ke liye use hoti hain.
# Common operations:
#   1. Erosion    → Object shrink, background expand
#   2. Dilation   → Object grow, holes fill
#   3. Opening    → Erosion + Dilation (noise remove small objects)
#   4. Closing    → Dilation + Erosion (small holes fill)
# OpenCV me `cv2.erode()`, `cv2.dilate()` use hote hain.

import cv2
import numpy as np
# Load grayscale image
image = cv2.imread('01.jpg' , 0)

# Define Kernel
kernel = np.ones((5,5), np.uint8 ) # 5x5 matrix of ones

# Apply Erosion
# Image ke objects ko chhota kar deta hai; foreground shrink hota hai aur small noise remove ho sakti hai.
img_erosion = cv2.erode(image , kernel , iterations=1)

# Apply Dilation
# Image ke objects ko bada kar deta hai; holes fill ho jati hain aur object grow hota hai
img_dilation = cv2.dilate(image , kernel , iterations=1)

# Apply Opening
# Erosion ke baad Dilation; small noise ya unwanted tiny objects remove karne ke liye use hota hai.
img_opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# Apply Closing
# Dilation ke baad Erosion; small holes fill karne aur object gaps close karne ke liye use hota hai.
img_closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)


cv2.imshow('Original Image ' , image)
cv2.imshow('Erosion ' , img_erosion)
cv2.imshow('Dilation' , img_dilation)
cv2.imshow('Opening ' , img_opening)
cv2.imshow('Closing' , img_closing)

if cv2.waitKey(0) & 0xff == ord('q'):
    cv2.destroyAllWindows()