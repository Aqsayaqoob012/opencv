'''
Edge detection ka matlab hai image ke sharp boundaries / outlines detect karna
Jahan pixel intensity achanak change hoti hai, wahan edge hota hai.

Edges object ki shape, size, aur position batate hain
Is liye image recognition & object detection mein bohat important hai

Parameters:
img → input image
100 → lower threshold
200 → upper threshold

Rule:
Gradient < 100 → ignore
Gradient > 200 → strong edge
Beech mein → agar strong edge se connected ho
'''
import cv2
image = cv2.imread('room2.jpg')

edges = cv2.Canny(image , 100 , 200)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
