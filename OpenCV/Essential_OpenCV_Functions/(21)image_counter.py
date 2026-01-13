# 1️⃣ Image Load
import cv2
import numpy as np

image = cv2.imread('card.png')

# 2️⃣ Convert to Grayscale
gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

# 3️⃣ Apply Gaussian Blur (Noise kam karne ke liye)
blur = cv2.GaussianBlur(gray , (5,5) , 0)

# 4️⃣ Edge Detection using Canny
edge = cv2.Canny(blur , 50 ,150)
cv2.imshow("Canny Edges", edge)


# 5️⃣ Find Contours
contours, hierarchy = cv2.findContours(
    edge , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE
)
# 6️⃣ Print number of contours found
print('Number Of Counters Found : ' , len(contours))

# 7️⃣ Draw Contours on Original Image
Contour_image = image.copy()
# -1 → Matlab “Draw all contours
cv2.drawContours(Contour_image , contours , -1, (0, 255, 0), 3) # green color, thickness 3

cv2.imshow("Contours", Contour_image)


# 8️⃣ Optional: Draw bounding boxes & contour area

for cnt in contours:
    # x, y → rectangle ka top-left corner  
    # w, h → rectangle ka width & height
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(Contour_image, (x,y), (x+w, y+h), (255,0,0), 2)  # blue rectangle
    area = cv2.contourArea(cnt)
    print("Contour Area:", area)

cv2.imshow("Contours with Bounding Boxes", Contour_image)
cv2.waitKey(0)
cv2.destroyAllWindows()