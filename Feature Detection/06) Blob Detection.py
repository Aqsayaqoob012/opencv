'''
1️⃣ Blob Detection kya hai?

Blob:
Non-technical definition: Ek thick liquid drop ya connected pixels ka group.
Technical definition: Image mein aise pixels ka cluster jahan intensity ya color similar ho aur connected ho.

Goal:
Identify whether a blob is a circle ya ellipse ya koi aur connected shape.
OpenCV ka SimpleBlobDetector function is kaam ke liye best hai.

2️⃣ Key Parameters in SimpleBlobDetector
OpenCV mein blob detect karte waqt filtering parameters define karte hain. Ye ensure karte hain ki sirf desired shapes detect ho.

a) Filter by Area
Small dots ya noise ko ignore karne ke liye.
Example: Agar sirf bade circles detect karne hain, toh minimum area set karte hain.

params.filterByArea = True
params.minArea = 100

b) Filter by Circularity
Shapes ko circle ke similar hone ke liye filter karta hai.

Formula:

Circularity = 4 𝜋 ⋅ Area  / Perimeter 2 
	​

Perfect circle → Circularity = 1
Square → Circularity ~ 0.78

params.filterByCircularity = True
params.minCircularity = 0.9

c) Filter by Convexity

Convexity = object ka smoothness aur concave regions ka absence.
Circle jitna smooth aur convex hoga → Convexity zyada.

params.filterByConvexity = True
params.minConvexity = 0.2

d) Filter by Inertia

Inertia ratio = shape ka elongation measure.
Circle → 1
Ellipse → 0 to 1
Line → 0

params.filterByInertia = True
params.minInertiaRatio = 0.01


Inertia ratio filter karne se aap circles aur ellipses easily distinguish kar sakte ho.
'''

import cv2
import numpy as np

# Load previously created image
img = cv2.imread("shape.png")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bitwise_not(gray)  # Invert colors: white circles on black

# Setup SimpleBlobDetector parameters
params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.minArea = 500
params.filterByCircularity = True
params.minCircularity = 0.7
params.filterByConvexity = True
params.minConvexity = 0.2
params.filterByInertia = True
params.minInertiaRatio = 0.5

# Create detector
detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs
keypoints = detector.detect(gray)

# Draw blobs as red circles
blank = np.zeros((1, 1)) 
blobs = cv2.drawKeypoints(img, keypoints, blank, (0, 0, 255),
                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Count detected blobs
number_of_blobs = len(keypoints)
print("Number of Circular Blobs:", number_of_blobs)

cv2.imshow("Detected Circular Blobs", blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''
4️⃣ Explanation of Code

cv2.imread() → Grayscale image load karna.
cv2.SimpleBlobDetector_Params() → Parameter object initialize karna.
filterByArea/Circularity/Convexity/Inertia → Blob ko desired shape ke hisaab se filter karna.
cv2.SimpleBlobDetector_create(params) → Detector create karna.
detector.detect(image) → Blob detection.
cv2.drawKeypoints() → Detected blobs ko red circles mein draw karna.
cv2.putText() → Total detected blobs ko image pe print karna.
cv2.imshow() → Final result show karna.

5️⃣ Key Notes
minArea ko adjust kar ke small noise ignore karo.
minCircularity ko adjust kar ke true circles detect karo.
Convexity aur inertia ratio optional hain, lekin detection zyada accurate hota hai.
Agar aap ellipses bhi detect karna chahte ho → circularity ko 0.5–0.9 range mein rakh sakte ho.

✅ Result:
Image mein detected circles red dots ke saath highlight honge.
Total circles ka count bhi image pe show hoga.
'''