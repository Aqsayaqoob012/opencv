import cv2
import numpy as np

# Create blank white image
img = np.ones((600, 600, 3), np.uint8) * 255

# Draw circles
cv2.circle(img, (100, 100), 50, (0, 0, 0), -1)   # Black filled circle
cv2.circle(img, (300, 100), 30, (0, 0, 255), -1) # Red filled circle

# Draw ellipses
cv2.ellipse(img, (200, 400), (50, 30), 0, 0, 360, (255, 0, 0), -1) # Blue ellipse
cv2.ellipse(img, (400, 400), (70, 40), 30, 0, 360, (0, 255, 0), -1) # Green tilted ellipse

# Save image
cv2.imwrite("shape.png", img)
cv2.imshow("Shape", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
