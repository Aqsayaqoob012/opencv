# Image rotation ka matlab hai image ko clockwise ya counter-clockwise ghumana.
# OpenCV me `cv2.getRotationMatrix2D()` aur `cv2.warpAffine()` use hota hai.
# Hum center, angle aur scale specify karte hain.

import cv2
image = cv2.imread('1.jpg')

h , w = image.shape[:2]
center = (h//2 , w//2)  # rotation ka center point

# 3. Rotation matrix banana
angle = 45  # ghumane ka angle (degrees)
scale = 1.0  # size maintain karna
M = cv2.getRotationMatrix2D(center, angle, scale) # rotation matrix banata hai jisma center , angle or scale hoty hain

# 4. Image rotate karna
rotated_image = cv2.warpAffine(image , M , (w,h)) # matrix apply karke image rotate karta hai.

cv2.imshow('Original Image' , image)
cv2.imshow('Rotated Image' , rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()