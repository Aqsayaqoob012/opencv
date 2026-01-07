import cv2
image = cv2.imread('01.jpg')

resize = cv2.resize(image , (275,183))  # (width, height)
cv2.imwrite('new_image.jpg' , resize)
cv2.imshow('original Image' , image)
cv2.imshow('Resized Image' , resize)
cv2.waitKey(0)
cv2.destroyAllWindows() 

'''
The problem with this approach is that the aspect ratio of the image is not maintained. So we need to do some extra work in order to maintain a proper aspect ratio.

Aspect Ratio image ki width aur height ka proportion hota hai.
 Ye batata hai ke image kitni lambi aur kitni chori hai.

'''
h, w = image.shape[:2]
# Calculating the ratio
new_width = 500 / w
# Creating a tuple containing width and height
new_height = (500, int(h * new_width))

# Resizing the image
resize_aspect = cv2.resize(image, new_height)
cv2.imshow("Resized Image", resize_aspect)
cv2.waitKey(0)
