import cv2 
image = cv2.imread('1.jpg')

blurred = cv2.GaussianBlur(image , (7,7) , 3)

cv2.imshow('original image ' , image)
cv2.imshow('Blured image' , blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
