'''
1️⃣ Harris Corner Detection kya hai?
Corners wo points hote hain jahan image ka intensity (brightness) multiple directions mein abruptly change hota hai.
Edges sirf ek direction mein change hoti hain.
Corners multiple directions mein change hoti hain, isliye wo zyada distinctive hote hain.
Usefulness of Corners:
Distinctive: Easily identifiable aur unique hote hain.
Stable: Image ko rotate ya scale karo, corners largely same rehte hain.
Reliable for Matching: Image stitching, 3D reconstruction, motion tracking ke liye useful.
Example: Agar ek building ka corner hai image mein, wo corner rotation ya scale ke baad bhi easily identifiable rahega.

2️⃣ Theory Behind Harris Corner Detection
Harris Corner Detection ka idea ye hai ki har pixel ke neighborhood ka intensity change analyze karte hain:
Ek window (block) ke andar gradient calculate karte hain:
Gradient = pixel intensity ka change.
Sobel operator ya derivative use karte hain.

Ye gradients matrix banata hain:
                                 (image 05)

3️⃣ Harris Corner Detection in OpenCV
OpenCV mein ye kaam cv2.cornerHarris() function karta hai.

Syntax:
cv2.cornerHarris(src, blockSize, ksize, k)

Parameters:
src: Input grayscale image
blockSize: Neighborhood ka size (zyaada bada → large corners detect)
ksize: Sobel operator ka kernel size (gradient calculation)
k: Harris formula ka free parameter (0.04-0.06)
Extra: cv2.dilate() ka use corners ko thoda highlight karne ke liye hota hai.
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Image load karna
image_path = "shapes.png"
image = cv2.imread(image_path)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)  # Harris function requires float32

# Harris corner detection
dest = cv2.cornerHarris(gray, blockSize=17, ksize=21, k=0.01)

# Dilate for better visibility
dest = cv2.dilate(dest, None)

# Mark corners in red
image[dest > 0.01 * dest.max()] = [0, 0, 255]

# Convert BGR to RGB for Matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display
plt.imshow(image_rgb)
plt.title('Harris Corner Detection')
plt.axis('off')
plt.show()
'''
Explanation of Code:

cv2.cvtColor() → image ko grayscale mein convert karna.
np.float32() → Harris function sirf float32 accept karta hai.
cv2.cornerHarris() → corner response calculate karta hai.
cv2.dilate() → corners ko visibly enlarge karna.
image[dest > 0.01*dest.max()] = [0,0,255] → high response corners ko red color mark karna.
plt.imshow() → final result display karna.

5️⃣ Output Example
Detected corners red dots mein visible honge.
Corners edge aur flat regions se easily distinguishable hote hain.

6️⃣ Advantages of Harris Corner Detection
Accuracy: Corners high precision se detect hotay hain.
Noise Resilience: Image mein thoda noise ho to bhi kaam karta hai.
Rotation & Scale Invariance: Rotated/scaled images mein corners stable rehte hain.
Foundation for Advanced Algorithms: SIFT, SURF, ORB jaisi methods ka base hai.

7️⃣ Challenges / Limitations
Parameter Sensitivity: Block size, Sobel kernel size aur k choose karna tricky ho sakta hai.
Computationally Expensive: Large images ya videos ke liye slow.
Flat Surfaces: Flat areas mein corners detect nahi hotay.
Real-Time Applications: Speed ke liye ideal nahi, kyunki heavy computation hai.

8️⃣ Notes / Tips
blockSize bada → large corners detect, slow performance
ksize bada → small intensity changes pe sensitive, noisy ho sakta hai
k chhota → strict corner detection, bada → loose corner detection
'''