'''
1️⃣ Foreground Extraction kya hai?
Foreground extraction ka matlab hai:
Image me main object (foreground) ko background se alag karna

Example: Image me Goku aur Vegeta characters hain → unko background se alag karna
Ye image editing, object recognition, aur image segmentation me useful hai.

2️⃣ GrabCut Algorithm ka Concept
GrabCut ek graph-cut based image segmentation algorithm hai, jo 2004 me introduce hua.

Kaam kaise karta hai:

User interaction:
Rectangle draw karo image ke around object
Ye rectangle object ko roughly enclose karta hai

Region of Interest (ROI):
Rectangle ke andar = unknown
Rectangle ke bahar = obvious background (black)

Gaussian Mixture Model (GMM):
Pixels ko foreground aur background ke clusters me divide karta hai
Har pixel ko color aur texture statistics ke basis par label karta hai

Graph Generation:
Har pixel = node
2 extra nodes: Source (foreground) aur Sink (background)
Foreground pixels connected to Source, Background pixels connected to Sink

Edge Weights:
Pixel aur Source/Sink ke edges ka weight = probability pixel foreground/background ka hai
Agar color difference zyada → low weight

Graph Segmentation:
Cost function minimize karke graph 2 parts me divide hota hai
Source se connected pixels → foreground
Sink se connected pixels → background

Iteration:
Algorithm multiple iterations chalata hai → segmentation refine hota hai

3️⃣ GrabCut in OpenCV
Function: cv2.grabCut()

Syntax:
cv2.grabCut(image, mask, rectangle, backgroundModel, foregroundModel, iterationCount[, mode])


Parameters:
image → Input image (BGR, 8-bit)
mask → Output mask (initialized as zeros)
0 = obvious background (GC_BGD)
1 = obvious foreground (GC_FGD)
2 = probable background (GC_PR_BGD)
3 = probable foreground (GC_PR_FGD)

rectangle → ROI around object
backgroundModel → Temporary array for background GMM
foregroundModel → Temporary array for foreground GMM
iterationCount → Algorithm kitni baar run kare

mode →
GC_INIT_WITH_RECT → Rectangle mode
GC_INIT_WITH_MASK → Mask mode
GC_EVAL → Resume
'''

import numpy as np
import cv2
from matplotlib import pyplot as plt

# Step 1: Image load karo
image = cv2.imread('images.jpg')

# Step 2: Mask initialize karo
mask = np.zeros(image.shape[:2], np.uint8)

# Step 3: Background aur foreground model initialize karo
backgroundModel = np.zeros((1, 65), np.float64)
foregroundModel = np.zeros((1, 65), np.float64)

# Step 4: Rectangle define karo (ROI)
# format: (startX, startY, width, height)
rectangle = (67, 2, 100, 200)

# Step 5: GrabCut algorithm apply karo
cv2.grabCut(image, mask, rectangle, backgroundModel, foregroundModel, 3, cv2.GC_INIT_WITH_RECT)

# Step 6: Final mask create karo
# 0 & 2 → background, 1 & 3 → foreground
mask2 = np.where((mask == 2)|(mask == 0), 0, 1).astype('uint8')

# Step 7: Foreground extract karo
image_segmented = image * mask2[:, :, np.newaxis]

# Step 8: Display original aur segmented image
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Segmented Image')
plt.imshow(cv2.cvtColor(image_segmented, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.show()


'''
5️⃣ Step by Step Explanation (Roman Urdu)
Image load → cv2.imread() se
Mask initialize → zeros (background aur foreground mark karne ke liye)
BackgroundModel & ForegroundModel → GMM ke liye temporary arrays
Rectangle define → object ke around rectangle draw karo
GrabCut call → cv2.grabCut() with 3 iterations
Mask refine → 0 & 2 = background, 1 & 3 = foreground
Foreground extract → mask * image → sirf object bacha
Display → matplotlib se original aur segmented image dikhaye

6️⃣ Notes / Observations
GrabCut efficiently foreground object extract karta hai
Complex objects (like Goku ka hair ya aura) → partially segmented ho sakta hai
Manual input (rectangle) chahiye → accuracy depend karti hai
Iterations badha kar segmentation refine kar sakte ho

🔑 Summary
Step	Function / Concept	  Matlab
1	Draw rectangle	         ROI decide karna
2	Initialize mask	         Pixels ko label karna
3	GMM	                     Pixel color statistics ke basis par cluster
4	Graph Generation	     Pixels = nodes, Source = foreground, Sink = background
5	Graph Cut	             Cost function minimize → segmentation
6	Extract foreground	     Mask * original image
7	Display	                 Original vs segmented
'''