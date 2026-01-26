'''
1️⃣ Sab se pehle sawal:
❓ Line detection ki zarurat kyun hoti hai?
Image processing mein hum aksar yeh kaam karte hain:
Road lanes detect karna
Barcode read karna
Document borders detect karna
Classroom / exam monitoring

Object boundaries nikalna
👉 In sab mein straight lines bohot important hoti hain.

2️⃣ Normal Line Equation problem kyun karti hai?
Normal equation:
y = mx + c

❌ Problem:
Vertical line ke liye m = ∞
Computer ke liye handle karna mushkil
Is liye OpenCV yeh equation use nahi karta

3️⃣ OpenCV wali Line Equation (MOST IMPORTANT)

OpenCV parametric form use karta hai:
r = x cos(θ) + y sin(θ)

Iska matlab:
r (rho) = origin se line ka perpendicular distance
θ (theta) = angle (x-axis se)
x, y = edge pixel ke coordinates

✅ Is equation se:
Horizontal
Vertical
Slanted
sab lines detect ho jati hain

4️⃣ Hough Transform ka core idea (Dil samjho)

👉 Image mein pixels hotay hain
👉 Line ek single pixel se nahi banti
👉 Line = bohot saray aligned pixels

Hough Transform yeh kaam karta hai:
“Kaun se pixels mil kar ek hi mathematical line ko vote kar rahe hain?”

5️⃣ Image Space → Hough Space
🔹 Image Space:
X, Y coordinates
Pixel based

🔹 Hough Space:

R (rho)
Θ (theta)

👉 Har pixel Hough space mein curve banata hai
👉 Jahan curves intersect hoti hain
➡️ wahan line exist karti hai

6️⃣ Accumulator Array (Voting System)

Hough Transform ek 2D array banata hai jisko kehte hain:
Accumulator[r][θ]

Initially:
Accumulator = 0

7️⃣ Accumulator ka size kaise banta hai?
🔸 Theta (θ):
Range = 0° → 180°
Agar 1 degree accuracy chahiye:
180 columns

🔸 Rho (r):
Max distance = image diagonal

Example:
Image = 100 × 100
Diagonal = √(100² + 100²) ≈ 141

So:
141 rows

👉 Final Accumulator:
141 × 180

8️⃣ Ab REAL working samjho (step-by-step)
Assume:
Image: 100×100
Center mein ek horizontal line

🔹 Step 1: Edge detection

Pehle image ko binary edge image banate hain
edges = cv2.Canny(gray, 50, 150)

🔹 Step 2: Edge pixel uthao

Har white pixel (x, y) jo edge par hai

🔹 Step 3: Theta loop

Har pixel ke liye:
θ = 0 → 180
Har θ par:
r = x cos(θ) + y sin(θ)

🔹 Step 4: Vote do

Har (r, θ) ke liye:
Accumulator[r][θ] += 1

🔹 Step 5: Repeat

Jitnay zyada pixels ek hi line par:
Utni hi baar
Same (r, θ) vote hota rahe ga

🔹 Step 6: Peak dhoondo

Accumulator mein:

Jahan maximum votes
➡️ woh actual line
9️⃣ Important concept (Point → Curve)

Image ka ek point
Hough space mein sinusoidal curve

👉 Multiple curves ka intersection
➡️ Strong line evidence

🔟 OpenCV Function: cv2.HoughLines()
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

Parameters deep explanation:
Parameter	Matlab
edges	    Binary image (Canny ke baad)
1	        Rho resolution (1 pixel)
np.pi/180	Theta resolution (1 degree)
200	         Minimum votes

👉 Threshold = minimum line length

1️⃣1️⃣ Output format
(r, θ)
r → pixels
θ → radians

1️⃣2️⃣ Line draw karne ka maths (VERY CRITICAL)

OpenCV (r, θ) deta hai
Hume 2 points chahiye

Formula:
a = cos(θ)
b = sin(θ)

x0 = r * a
y0 = r * b

x1 = x0 + 1000*(-b)
y1 = y0 + 1000*(a)

x2 = x0 - 1000*(-b)
y2 = y0 - 1000*(a)

👉 1000 = infinite line feel dene ke liye
'''

import cv2
import numpy as np

# Read image
image = cv2.imread('download (1).jpg')

# Convert image to grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# Use canny edge detection
edges = cv2.Canny(gray,50,150,apertureSize=3)

# Apply HoughLinesP method to 
# to directly obtain line end points
lines_list =[]
lines = cv2.HoughLinesP(
            edges, # Input edge image
            1, # Distance resolution in pixels
            np.pi/180, # Angle resolution in radians
            threshold=100, # Min number of votes for valid line
            minLineLength=5, # Min allowed length of line
            maxLineGap=10 # Max allowed gap between line for joining them
            )

# Iterate over points
for points in lines:
      # Extracted points nested in the list
    x1,y1,x2,y2=points[0]
    # Draw the lines joing the points
    # On the original image
    cv2.line(image,(x1,y1),(x2,y2),(0,255,0),2)
    # Maintain a simples lookup list for points
    lines_list.append([(x1,y1),(x2,y2)])
    
# Save the result image
cv2.imwrite('detectedLines.png',image)

'''

1️⃣4️⃣ HoughLinesP (Probabilistic – Easy & Fast)
Difference samjho:

| HoughLines     | HoughLinesP  |
| -------------- | ------------ |
| Infinite line  | Line segment |
| r, θ output    | x1,y1,x2,y2  |
| Heavy          | Fast         |
| Maths required | Direct draw  |

1️⃣5️⃣ Summary (Exam + Interview Ready)

Line pixels known hotay hain
(r, θ) unknown hotay hain
Hough Transform voting karta hai
Accumulator peaks → lines
Noise tolerant
Broken lines detect karta hai

1️⃣6️⃣ Real-World Uses

✔️ Road lane detection
✔️ Barcode scanners
✔️ OCR systems
✔️ Surveillance
✔️ Medical imaging
✔️ Industrial vision

'''
