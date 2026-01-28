'''🔷 Find Co-ordinates of Contours using OpenCV (Theory)
🔹 Contour kya hota hai?

Contour asal me:

Object ki boundary / outline hoti hai

Ye un points ko connect karta hai jahan:

Color same ho

Ya intensity same ho

📌 Simple words me:

Contour kisi object ka shape represent karta hai

🔹 Contours kyun important hain?

Contours ka use hota hai:

Object detection

Shape recognition

Area & perimeter calculation

Object tracking

Orientation (arrow tip, direction)

Image analysis

🔹 OpenCV me contours kaise milte hain?

OpenCV ek function provide karta hai:

cv2.findContours()


Ye function:

Image se boundary points nikalta hai

Har contour ko NumPy array ki form me return karta hai

Jisme har point ke (x, y) coordinates hote hain

🔹 Overall Approach (Logic Flow)

1️⃣ Image read karo (color + grayscale)
2️⃣ Grayscale image ko binary banao
3️⃣ Binary image se contours detect karo
4️⃣ Contours ko approximate karo
5️⃣ Contours ko image par draw karo
6️⃣ Contour ke coordinates extract karo
7️⃣ Coordinates ko image par label karo

🟢 Step-by-Step Theory Explanation
🟩 Step 1: Image Read Karna
img2 = cv2.imread('test.jpg', cv2.IMREAD_COLOR)
img = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)


📌 Yahan:

img2 → Color image (drawing & labeling ke liye)

img → Grayscale image (processing ke liye)

✔ Contours detection grayscale image par zyada effective hoti hai

🟩 Step 2: Image ko Binary banana (Thresholding)
_, threshold = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)


📌 Thresholding ka matlab:

Pixel value > 110 → White (255)

Pixel value ≤ 110 → Black (0)

✔ Binary image zaroori hoti hai
✔ Contours sirf white objects pe detect hote hain

🟩 Step 3: Contours Detect Karna
contours, _ = cv2.findContours(
    threshold,
    cv2.RETR_TREE,
    cv2.CHAIN_APPROX_SIMPLE
)

🔸 Parameters explanation:
Parameter	Matlab
threshold	Binary image
RETR_TREE	Contour hierarchy maintain
CHAIN_APPROX_SIMPLE	Extra points remove

📌 Output:

contours → List of contours

Har contour → points ka array

🟩 Step 4: Contour Approximation
approx = cv2.approxPolyDP(
    cnt,
    0.009 * cv2.arcLength(cnt, True),
    True
)


📌 Approximation ka matlab:

Contour ko simple polygon me convert karna

Extra unnecessary points hata dena

✔ Shape clear ho jata hai
✔ Coordinates kam aur meaningful hote hain

🟩 Step 5: Contours Draw Karna
cv2.drawContours(img2, [approx], 0, (0, 0, 255), 5)


📌 Red color contour:

Object ka outline visually show karta hai

🟩 Step 6: Coordinates Extract Karna
n = approx.ravel()


📌 ravel():

2D array ko 1D array me convert karta hai

Example:

[x1, y1, x2, y2, x3, y3, ...]

🟩 Step 7: (x, y) Coordinates Label Karna
if i % 2 == 0:
    x, y = n[i], n[i + 1]


📌 Logic:

Even index → x

Next value → y

Har point ka coordinate image par likha jata hai

🟩 First Coordinate ka Special Use
if i == 0:
    cv2.putText(img2, "Arrow tip", (x, y), ...)


📌 Note:

First coordinate aksar topmost point hota hai

Iska use hota hai:

Arrow direction

Object orientation

Shape alignment

🟩 Final Output
cv2.imshow('Contours with Coordinates', img2)


Result:

Object boundary visible

Har vertex ke coordinates image par likhe hue

✅ Advantages of Using Contours

✔ Exact object boundary
✔ Shape analysis possible
✔ Coordinates easily available
✔ Fast & efficient
✔ No deep learning required

❌ Limitations

❌ Noise ho to wrong contours
❌ Lighting changes affect result
❌ Overlapping objects me issue
❌ Proper threshold zaroori

🔚 Summary (Exam-Ready)

Contours object ki boundaries hoti hain jo image processing me shape analysis
 ke liye use hoti hain. OpenCV ka cv2.findContours() function image se contours
   extract karta hai aur unke exact (x, y) coordinates provide karta hai.
     In coordinates ko shape detection, area calculation, orientation aur object recognition
       jaise tasks me use kiya jata hai.'''

import numpy as np
import cv2

font = cv2.FONT_HERSHEY_COMPLEX

# Load image
img2 = cv2.imread('test.jpg', cv2.IMREAD_COLOR)
img = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)

# Binarize image
_, threshold = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    # Approximate and draw contour
    approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)
    cv2.drawContours(img2, [approx], 0, (0, 0, 255), 5)

    # Flatten points
    n = approx.ravel()
    i = 0
    for j in n:
        if i % 2 == 0:  # x, y coords
            x, y = n[i], n[i + 1]
            coord = f"{x} {y}"
            if i == 0:  # first point
                cv2.putText(img2, "Arrow tip", (x, y), font, 0.5, (255, 0, 0))
            else:
                cv2.putText(img2, coord, (x, y), font, 0.5, (0, 255, 0))
        i += 1

# Show result
cv2.imshow('Contours with Coordinates', img2)

# Exit on 'q'
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()