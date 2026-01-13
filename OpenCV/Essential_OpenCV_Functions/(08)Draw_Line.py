# OpenCV me hum `cv2.line()` use karke image par line draw kar sakte hain.
# Required parameters: image, bottom-left corner co-ordinates, Bottom-right corner co-ordinates , color (BGR), thickness

import cv2
image = cv2.imread('1.jpg')

'''Image 
bottom-left corner co-ordinates
Bottom-right corner co-ordinates
Color (in BGR format)
Line width'''

bottom_left = (150,100)
bottom_right = (250,100)
color = (255,0,0)
line_width = 4

output = image.copy()
cv2.line(output , bottom_left , bottom_right , color  , line_width)
cv2.imshow('Draw a Line' , output)
cv2.waitKey(0)
cv2.destroyAllWindows()