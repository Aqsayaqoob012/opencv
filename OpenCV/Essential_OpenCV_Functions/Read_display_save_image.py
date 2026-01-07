import cv2
image = cv2.imread('01.jpg')

if image is not None:
    print('Load Successfully')
    success = cv2.imwrite('output.jpg' , image)
    cv2.imshow('First Image' , image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print('Image Not Found')    