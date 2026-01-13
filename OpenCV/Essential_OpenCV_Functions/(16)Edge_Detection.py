'''
Edge detection ka matlab hai image ke sharp boundaries / outlines /  object ke edges detect karna
Jahan pixel intensity achanak change hoti hai, wahan edge hota hai.

OpenCV me popular method Canny Edge Detection hai: cv2.Canny()

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

# Grayscale conversion (Canny ke liye zaruri)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(image , 100 , 200) # Ye edges detect kar ke binary image return karta hai (edges white, background black).
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
