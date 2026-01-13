# Image blurring ka matlab hai image ka smooth version create karna, jisme noise kam ho.
# OpenCV me popular methods:
#   1. cv2.GaussianBlur()   → Gaussian filter
#   2. cv2.blur()           → Average blur
#   3. cv2.medianBlur()     → Median blur (noise reduction ke liye best)
# Kernel size (k,k) jitna bada hoga, blur utna zyada hoga.

import cv2
image = cv2.imread('01.jpg')

# Gaussian Blur 

Gaussian_Blur = cv2.GaussianBlur(image , (7,7) , 0)  # kernel size (odd) , sigma (0 = auto)

#  Median Blur
# Median of surrounding pixels, salt-and-pepper noise ke liye best
Median_Blur = cv2.medianBlur(image , 5)     # kernel size (sirf ek number, odd)

# Bilateral Blur
Bilateral_Blur = cv2.bilateralFilter(image , 9, 75, 75) # diameter ,sigmaColor , sigmaSpace

cv2.imshow('Original Image' , image)
cv2.imshow('Gaussian Blur' , Gaussian_Blur)
cv2.imshow('Median Blur' , Median_Blur)
cv2.imshow('Bilateral Blur' , Bilateral_Blur)


if cv2.waitKey(0) & 0xff == ord('q'):
    cv2.destroyAllWindows()



