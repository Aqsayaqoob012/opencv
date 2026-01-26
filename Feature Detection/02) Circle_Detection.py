'''
1️⃣ Circle Detection kya hota hai?

Circle Detection ka matlab hai image ke andar:
gol cheezain (circles)
unka center (x, y)
aur radius (r)
automatically find karna.

Real-life uses:
👁 Eye / iris detection
🧪 White blood cells detection
🤖 Robotics (wheels, buttons)
🏭 Quality inspection
🎯 Object tracking

2️⃣ Circle ka Mathematical Concept (VERY IMPORTANT)

2D plane mein circle equation hoti hai:
(x − h)² + (y − k)² = r²

Yahan:
h → x-coordinate of center
k → y-coordinate of center
r → radius

👉 Matlab:
Aik circle ko define karne ke liye 3 cheezain chahiye:
(h, k, r)

3️⃣ Circle Detection mushkil kyun hoti hai?

Line detection mein:
(r, θ) → 2 parameters

Circle detection mein:
(h, k, r) → 3 parameters


👉 Is liye:
Search space 3D ho jata hai
Computation heavy ho jati hai

4️⃣ Classical Hough Transform for Circles (Concept)
Agar hum manual karein:
Image ko preprocess karo
Edge pixels nikaalo
3D accumulator banao (h, k, r)
Har edge pixel vote kare
Jahan max votes → wahan circle
❌ Yeh bohot slow hota hai

5️⃣ OpenCV ka Smart Solution
🔥 HOUGH_GRADIENT method
OpenCV HOUGH_GRADIENT use karta hai jo:
Edge direction (gradient) use karta hai
3D search ko reduce karta hai
Fast + accurate hota hai

👉 Is liye hum directly:

cv2.HoughCircles()
use karte hain.

6️⃣ cv2.HoughCircles() Function Syntax
cv2.HoughCircles(
    image,
    method,
    dp,
    minDist,
    param1,
    param2,
    minRadius,
    maxRadius
)

7️⃣ Har Parameter ko DETAIL mein samjho
🔹 image

Grayscale image
Color image allowed nahi

🔹 method
cv2.HOUGH_GRADIENT


✔️ Fast
✔️ Optimized
✔️ Recommended

🔹 dp (IMPORTANT)
dp = inverse ratio of accumulator resolution

dp	Matlab
1	Same resolution as image
2	Half resolution (fast but less accurate)

👉 Mostly:
dp = 1

🔹 minDist
Minimum distance between circle centers
👉 Overlapping circles avoid karta hai

Example:
minDist = 100

🔹 param1

Canny edge detector ka upper threshold
Lower threshold = param1 / 2

Example:
param1 = 100

🔹 param2 (MOST CRITICAL)
Accumulator threshold

param2	Result
High	Kam circles (strict)
Low	Zyada circles (false positives)
🔹 minRadius / maxRadius

Radius ki range limit karta hai

Noise kam karta hai

8️⃣ COMPLETE WORKING FLOW
Step 1: Image read
Step 2: Copy image
Step 3: Gray conversion
Step 4: Noise removal
Step 5: Circle detection
Step 6: Draw circle + center
'''
'''
import cv2
import numpy as np

# Read image
img = cv2.imread("eye.jpg")
output = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Reduce noise
gray = cv2.medianBlur(gray, 5)

# Detect circles
circles = cv2.HoughCircles(
    gray,
    cv2.HOUGH_GRADIENT,
    dp=1,
    minDist=100,      
    param1=100,         
    param2=40,       
    minRadius=30,       
    maxRadius=60
)

# Draw only the first detected circle
if circles is not None:
    circles = np.uint16(np.around(circles))
    x, y, r = circles[0][0]
    cv2.circle(output, (x, y), r, (0, 255, 0), 2)  # Circle outline
    cv2.circle(output, (x, y), 2, (0, 0, 255), 3)  # Center point

# Show result
cv2.imshow('Detected Circle', output)
cv2.waitKey(0)
cv2.destroyAllWindows() '''

import cv2
import numpy as np

img = cv2.imread("eye.jpg")
if img is None:
    print("Eye image load nahi hui")
    exit()

output = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.equalizeHist(gray)
gray = cv2.GaussianBlur(gray, (9,9), 2)

circles = cv2.HoughCircles(
    gray,
    cv2.HOUGH_GRADIENT,
    dp=1.5,
    minDist=gray.shape[0]//3,
    param1=120,
    param2=35,
    minRadius=30,
    maxRadius=80
)

if circles is not None:
    circles = np.uint16(np.around(circles))
    x, y, r = circles[0][0]

    cv2.circle(output, (x, y), r, (0,255,0), 2)
    cv2.circle(output, (x, y), 2, (0,0,255), 3)
    print("✅ Iris detected")
else:
    print("❌ Iris detect nahi hui")

cv2.imshow("Detected Iris", output)
cv2.waitKey(0)
cv2.destroyAllWindows()

