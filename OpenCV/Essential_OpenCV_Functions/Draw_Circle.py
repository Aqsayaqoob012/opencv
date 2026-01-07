import cv2
image = cv2.imread('1.jpg')

'''Image 
Center point
Radius
Color (in BGR format)
Line width'''

Center_point = (215,60)
Radius =40
color = (255,0,0)
line_width = 4

output = image.copy()
cv2.circle(output , Center_point , Radius , color  , line_width)
cv2.imshow('Draw a Circle' , output)
cv2.waitKey(0)
cv2.destroyAllWindows()