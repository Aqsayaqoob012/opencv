# Har pixel me 3 channels hote hain: Blue, Green, Red (BGR in OpenCV)
# Hum specific pixel ke B, G, R values nikal sakte hain using array indexing.
# Image ko read kar ke numpy array ke tarah access karte hain.

import cv2 
image = cv2.imread('01.jpg')

'''
OpenCV RGB nahi, BGR use karta hai
Index 0 → Blue
Index 1 → Green
Index 2 → Red '''

#  Pixel location specify karna
x = 50  # column (width)
y = 100 # row (height)

#  Pixel values extract karna
(R , G , B) = image[y , x ]

# image ke 100th row aur 50th column wala pixel select ho raha ha
# OpenCV me channel order BGR hai, isliye unpack karte hain (B, G, R).
print('R : {} , G : {} , B : {}' . format(R,G,B))

# Sirf ek channel ki value nikalna
# Blue
B = image[100,100,0]
print('B : {}' .format(B))
# Red
R = image[100,100,2]
print('R : {}' .format(R))