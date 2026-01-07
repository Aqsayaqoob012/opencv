import cv2
image = cv2.imread('01.jpg')
if image is None:
  print('Error : image is not found')
else:
  print('image loaded successfully') 

if image is not None:
  cv2.imshow('First image', image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

else:
  print('Could not load the image')