import numpy as np
import cv2

image1 = cv2.imread('room1.jpg')
image2 = cv2.imread('resized_room2.jpg')


subtracted_image = cv2.subtract(image1 , image2)

cv2.imshow('subtracted_image' , subtracted_image)

if cv2.waitKey(0) & 0xff == ord('q'):
    print('Quitting ....')
    cv2.destroyAllWindows()