'''Image
Text to be displayed
Bottom-left corner co-ordinates, from where the text should start
Font
Font size
Color (BGR format)
Line width '''

import cv2
image = cv2.imread('1.jpg')
font = cv2.FONT_HERSHEY_SIMPLEX
text = 'Hello'
font_size = 1
Bottom_left = (150,25)

color =(255,0,0)
line_width = 2
output = image.copy()
cv2.putText(output , text  , Bottom_left ,font ,font_size , color  , line_width)
cv2.imshow('Draw a Circle' , output)
cv2.waitKey(0)
cv2.destroyAllWindows()