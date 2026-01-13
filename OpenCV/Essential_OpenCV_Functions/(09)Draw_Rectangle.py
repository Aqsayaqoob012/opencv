# OpenCV me `cv2.rectangle()` use karke image par rectangle draw kar sakte hain.
# Required parameters: image, top-left corner, bottom-right corner, color (BGR), thickness


import cv2
image = cv2.imread('1.jpg')

'''Image 
Top-left corner co-ordinates
Bottom-right corner co-ordinates
Color (in BGR format)
Line width'''

top_left = (180,25)
bottom_right = (250,100)
color = (255,0,0)
line_width = 4

output = image.copy()
cv2.rectangle(output , top_left , bottom_right , color  , line_width)
cv2.imshow('Draw a rectangle' , output)
cv2.waitKey(0)
cv2.destroyAllWindows()