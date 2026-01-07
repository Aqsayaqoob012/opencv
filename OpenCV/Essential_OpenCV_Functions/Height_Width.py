import cv2

image = cv2.imread('01.jpg')

if image is not None:
    h ,w ,c = image.shape
    print("Height = {} , Width = {} , Channel = {}".format(h , w , c))
else :
    print('Image not found')   

# Only for Height and Width
'''if image is not None:
    h ,w  = image.shape[:2]
    print("Height = {} , Width = {} ".format(h , w))
else :
    print('Image not found')  '''


