'''Image translation ka matlab hai image ko left, right, up, ya down shift karna
Image rotate ya scale nahi hoti, sirf position change hoti hai.
Right move → tx
Down move → ty
Agar original pixel:  (x, y)

To new position hogi: x' = x + tx   ,  y' = y + ty

OpenCV mein translation ke liye matrix yeh hoti hai: | 1   0   tx |
                                                     | 0   1   ty |  Matrix float32 honi chahiye
'''
import numpy as np
import cv2
image = cv2.imread('room1.jpg')

row , col = image.shape[:2]
tx = 10 # right shift
ty = 20  # down shift

M = np.float32([
    [1 , 0 , tx],
    [0 , 1 , ty]
])

translated = cv2.warpAffine(image , M , ( col + tx , row + ty))

cv2.imshow("Original", image)
cv2.imshow("Translated Image", translated)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
 Direction Control
Movement	tx	ty
Right	+	0
Left	−	0
Down	0	+
Up	0	−
 
 '''