import cv2
import numpy as np

image1 = cv2.imread('car1.jpg')
image2 = cv2.imread('car2.jpg')

image1 = cv2.resize(image1 , (650 , 650))
image2 = cv2.resize(image2 , (650 , 650))

# Convert to Grayscale
gray1 = cv2.cvtColor(image1 , cv2.COLOR_BGR2GRAY )
gray2 = cv2.cvtColor(image2 , cv2.COLOR_BGR2GRAY)

# ORB Keypoints & Descriptors
orb = cv2.ORB_create(nfeatures = 1000) #  jitne zyada keypoints, utna better matching

kp1 , des1 = orb.detectAndCompute(gray1 , None)
kp2 , des2 = orb.detectAndCompute(gray2 , None)

# Brute-Force Matcher with Hamming distance

bf = cv2.BFMatcher(cv2.NORM_HAMMING , crossCheck=True)
matches = bf.match(des1 , des2)

# Sort Matches by Distance (Best first)
matches = sorted(matches , key = lambda x : x.distance)

# Draw Top Matches
match_image = cv2.drawMatches(
    image1 , kp1 , 
    image2 , kp2 ,
    matches[:20] , None,
    cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS
)

# # Resize for better visualization
match_image = cv2.resize(match_image , (1000,650))

cv2.imshow("Final Image" ,match_image)
cv2.waitKey(0)
cv2.destroyAllWindows()