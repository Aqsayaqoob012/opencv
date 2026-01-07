import cv2
image = cv2.imread('1.jpg')

# Color image ko black & white me convert karta hai 
grey = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

# BGR → RGB
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

cv2.imshow('Original Image' , image)
cv2.imshow('Grey' , grey)
cv2.imshow('RGB' , rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
