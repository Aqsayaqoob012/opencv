'''
🔺 Corner Detection kya hoti hai?

Corner wo jagah hoti hai jahan:

pixel intensity x direction aur y direction dono mein achanak change ho

jaise:
┗ L-shape
┏ box ka kona
┼ intersection

👉 Corners stable hote hain, is liye:

object tracking

panorama

feature matching
mein use hote hain

🧠 Shi-Tomasi Method (OpenCV)

OpenCV ka function:

cv2.goodFeaturesToTrack()


Ye image ke best & strong corners automatically choose karta hai.

🧩 Function ka simple matlab
corners = cv2.goodFeaturesToTrack(
    image,
    maxCorners,
    qualityLevel,
    minDistance
)

🔍 Parameters easy language mein
Parameter	Matlab
image	Grayscale image (color nahi)
maxCorners	Kitne corners chahiye (max limit)
qualityLevel	Corner ki strength (0–1)
minDistance	Do corners ke darmiyan minimum distance
🛠 STEP-BY-STEP CODE (FULL & CLEAN)
✅ Step 1: Libraries import karo
import cv2
import numpy as np
from matplotlib import pyplot as plt

✅ Step 2: Image load + grayscale
img = cv2.imread("corner1.png")

if img is None:
    print("Image load nahi hui")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


📌 Note:
Corner detection sirf intensity dekhta hai, color bekaar hai.

✅ Step 3: Corners detect karo (Shi-Tomasi)
corners = cv2.goodFeaturesToTrack(
    gray,
    maxCorners=27,
    qualityLevel=0.01,
    minDistance=10,
    blockSize=3,
    useHarrisDetector=False
)

🔎 Iska matlab:

27: zyada se zyada 27 corners

0.01: weak corners bhi allow

10 px: corners chipke hue nahi honge

Shi-Tomasi method use ho raha hai

❗ Important Check (VERY IMPORTANT)
if corners is None:
    print("No corners detected")
    exit()

✅ Step 4: Corners draw karo
corners = np.intp(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(
        img,
        (x, y),
        radius=4,
        color=(0, 255, 0),
        thickness=-1
    )

🟢 Yahan kya ho raha hai?

ravel() → (x, y) nikalta hai

thickness = -1 → filled circle

Green dots = detected corners

✅ Step 5: Result show karo
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Corners Detected (Shi-Tomasi)")
plt.axis("off")
plt.show()

📌 COMMON PROBLEMS & SOLUTIONS
❌ Corners zyada aa rahe hain?
qualityLevel=0.05

❌ Corners kam aa rahe hain?
qualityLevel=0.005

❌ Corners chipak rahe hain?
minDistance=20

🆚 Shi-Tomasi vs Harris
Shi-Tomasi	Harris
Stable	Sensitive
Default OpenCV	Manual tuning
Recommended	Advanced cases
🎯 SUMMARY (Yaad rakhna)

✔ Grayscale image
✔ goodFeaturesToTrack()
✔ qualityLevel control karta hai strength
✔ minDistance overlap rokta hai
✔ cv2.circle() se corners draw
'''


import cv2
import numpy as np
from matplotlib import pyplot as plt

# 1️⃣ Image load karo
img = cv2.imread('shapes.png')   # apni image ka correct path do

if img is None:
    print("❌ Image load nahi hui, path check karo")
    exit()

# 2️⃣ Grayscale conversion
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3️⃣ Corner detection (Shi-Tomasi)
corners = cv2.goodFeaturesToTrack(
    gray,
    maxCorners=50,      # maximum corners
    qualityLevel=0.01,  # chota value = zyada corners
    minDistance=10,     # corners ke darmiyan gap
    blockSize=3
)

# 4️⃣ Agar corners mil jayein to draw karo
if corners is not None:
    corners = np.intp(corners)
    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(
            img,
            (x, y),
            radius=4,
            color=(0, 255, 0),  # green
            thickness=-1       # filled circle
        )
else:
    print("⚠️ Koi corner detect nahi hua")

# 5️⃣ Show image using matplotlib
plt.figure(figsize=(6, 6))
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Corners Detected (Shi-Tomasi)")
plt.axis('off')
plt.show()
'''
🔍 Important Notes (ye bohot common mistakes hoti hain)
❗ Image load nahi ho rahi
img is None ka matlab:
Path ghalat
Image us folder mein nahi

❗ Bohot zyada / kam corners
Zyada corners → qualityLevel = 0.01
Kam corners → qualityLevel = 0.1
Overlapping rokne ke liye minDistance barhao

❗ Eye image mein corners kam aate hain
Eye smooth aur round hoti hai, isliye:
Corner detection kam effective hota hai
Eye ke liye Hough Circle Transform zyada best hota hai
'''