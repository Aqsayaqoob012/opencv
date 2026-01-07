import cv2 
image = cv2.imread('01.jpg')

'''
OpenCV RGB nahi, BGR use karta hai
Index 0 → Blue
Index 1 → Green
Index 2 → Red '''

(R , G , B) = image[100, 100]

# image ke 100th row aur 100th column wala pixel select ho raha ha

print('R : {} , G : {} , B : {}' . format(R,G,B))

# Sirf ek channel ki value nikalna
# Blue
B = image[100,100,0]
print('B : {}' .format(B))
# Red
R = image[100,100,2]
print('R : {}' .format(R))