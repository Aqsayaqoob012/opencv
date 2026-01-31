# Contours ka matlab hai image me objects ke boundaries detect karna.
# OpenCV me contours find karne ke liye:
#   1. Grayscale conversion
#   2. Apply Gaussian Blur (Noise kam karne ke liye)
#   3. Threshold ya Canny edge detection
#   4. cv2.findContours() use karte hain
#   5. cv2.drawContours() se draw karte hain

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
    edge , cv2.RETR_EXTERNAL
      , cv2.CHAIN_APPROX_SIMPLE
)
# cv2.CHAIN_APPROX_SIMPLE => Contour ke points ko compress karke store karta hai, unnecessary points ko remove karta hai.
#  cv2.RETR_EXTERNAL => Sirf external (outer) contours detect karta hai, inner contours ignore karta hai.
#cv2.RETR_TREE – Saare contours (outer + inner) detect karta hai aur parent-child relationship bhi maintain karta hai.
# cv2.RETR_CCOMP – Contours ko 2 levels (external + internal) me organize karta hai.
'''
contours
Ye ek list of all detected contours hai.
Har contour Numpy array of points hota hai, jo us boundary ke coordinates batata hai.

Example structure:
contours[0]
# array([[x1, y1], [x2, y2], [x3, y3], ...])
Matlab: har contour ke sare points store hote hain.

2️⃣ hierarchy
Ye contours ke relationships ko describe karta hai (parent, child, next, previous).
'''

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