import cv2
image = cv2.imread('1.jpg')

h , w = image.shape[:2]
center = (h//2 , w//2)

M = cv2.getRotationMatrix2D( center , 45 , 1)
rotated_image = cv2.warpAffine(image , M , (w,h))

cv2.imshow('Original Image' , image)
cv2.imshow('Rotated Image' , rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()