'''1️⃣ Image Registration kya hai?

Image registration matlab:
Do ya zyada images ko ek dusre ke sath align karna, takay wo same plane ya same angle me match karein.

Example:
Aap ek book ka photo alag-alag angles se lete ho.
Reference image = perfect angle
Dusri images ko is reference ke angle ke saath align karna = image registration

2️⃣ Image Registration ka kaam kaise hota hai?
Grayscale me convert karna
Color zaroori nahi, feature matching grayscale me hi hota hai.

Keypoints aur descriptors nikalna
Keypoints = images ke “standout points” (jaise corner, edge)
Descriptors = keypoints ka feature representation (histogram ya gradient)
OpenCV me ORB use hota hai:
ORB = Oriented FAST + Rotated BRIEF
Fast aur free algorithm hai, patent-free

Keypoints match karna
BFMatcher (Brute Force Matcher) use hota hai
Ye best matching points ko find karta hai
Top matches select karna
Sirf best matches rakhte hain
Noisy points hata dete hain
Homography find karna
Homography = 3x3 transformation matrix
Ye bataata hai kaise image ko reference ke plane me shift / rotate / scale karna hai
Transform apply karna
cv2.warpPerspective() se original image ko reference ke plane me align karte hain''' 

import cv2
import numpy as np

# Step 1: Images load
img_to_align = cv2.imread("book1.webp")
ref_img = cv2.imread("book1.webp")

# Step 2: Grayscale me convert
img1 = cv2.cvtColor(img_to_align, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(ref_img, cv2.COLOR_BGR2GRAY)

# Step 3: ORB detector create karo
orb = cv2.ORB_create(5000)

# Step 4: Keypoints aur descriptors find karo
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# Step 5: Feature matching using BFMatcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)

# Step 6: Matches sort karo
matches = sorted(matches, key=lambda x: x.distance)

# Step 7: Top 90% matches select
matches = matches[:int(len(matches)*0.9)]

# Step 8: Keypoints coordinates prepare
pts1 = np.zeros((len(matches), 2))
pts2 = np.zeros((len(matches), 2))
for i, match in enumerate(matches):
    pts1[i, :] = kp1[match.queryIdx].pt
    pts2[i, :] = kp2[match.trainIdx].pt

# Step 9: Homography calculate
homography, mask = cv2.findHomography(pts1, pts2, cv2.RANSAC)

# Step 10: Transform apply
aligned_img = cv2.warpPerspective(img_to_align, homography, (img2.shape[1], img2.shape[0]))

# Step 11: Save aur display
cv2.imwrite("aligned_output.jpg", aligned_img)
cv2.imshow("Aligned", aligned_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
Step by Step 

cv2.imread() → images ko load karna
cv2.cvtColor(..., cv2.COLOR_BGR2GRAY) → grayscale conversion
ORB_create(5000) → ORB detector create, 5000 features search karega
detectAndCompute() → keypoints aur descriptors nikalna
BFMatcher() → features match karna
matches.sort() → distance ke basis pe best matches select
matches[:90%] → noisy matches hataana
Keypoints coordinates store → pts1 aur pts2
cv2.findHomography() → transformation matrix nikalna
cv2.warpPerspective() → image ko reference ke plane me shift / rotate / scale
cv2.imwrite() → aligned image save karna

🔑 Important Notes
ORB is fast aur patent-free
BFMatcher with Hamming distance best for ORB
Homography = 3x3 matrix, jo shift/rotate/scale ka formula deta hai
RANSAC = outliers remove karta hai
'''