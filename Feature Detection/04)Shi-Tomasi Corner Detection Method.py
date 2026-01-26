'''
🔹 1. Corner Detection kya hai?

Corner: Image ka wo point jahan pixel intensity dono directions mein achanak change hoti ho.

Example:

Ek L-shape ya box ka kona → strong corner
Flat area → no corner
Edge → ek direction mein change hai, doosri mein nahi → corner nahi
Corner detection feature detection ka base hai, jise:
Image stitching (panorama)
Motion tracking
Object recognition
me use kiya jata hai.

🔹 2. Shi-Tomasi Method kyun?
Shi-Tomasi ek improved version of Harris Corner Detection hai.

Advantages:
Fast & Efficient: Computation kam aur fast
Accurate: Strong corners accurately detect karta hai
Robust: Noisy ya textured images mein bhi kaam karta hai

🔹 3. Theory / Mathematics
Step 1: Small Window Scan
Image ke chhote window (W x W) ko scan karte hain
Har window mein intensity change dekha jata hai

Intensity change formula:
 𝑓 ( 𝑋 , 𝑌 ) = ∑ ( 𝐼 ( 𝑋 𝑘 , 𝑌 𝑘 ) − 𝐼 ( 𝑋 𝑘 + Δ 𝑋 , 𝑌 𝑘 + Δ 𝑌 ) ) 2 

(X k 	​ ,Y k 	​ ) → pixel coordinates window ke andar
ΔX,ΔY → pixel shift
Agar intensity change dono directions mein zyada → corner

Step 2: Taylor Expansion
Direct calculation heavy hota hai → simplify karte hain
Eigenvalues ( 𝜆 1 , 𝜆 2 λ 1 	​ ,λ 2 	​ ) nikalte hain

Corner response:
𝑅 = min ⁡ ( 𝜆 1 , 𝜆 2 )
R= min ( λ 1 	​ ,λ 2 	)

R high → corner strong
Small / zero → edge ya flat region

Step 3: Corner Detection
Compare R values
Jo R sab se high → strongest corners select
Shi-Tomasi algorithm best corners ko select karta hai (top N strongest)
OpenCV me yeh function hai:
cv2.goodFeaturesToTrack(gray_img, maxCorners, qualityLevel, minDistance)

🔹 4. Parameters ka matlab
Parameter	                  Matlab
gray_img	               Grayscale input image
maxCorners	               Maximum corners detect karne hain
qualityLevel	           Minimum accepted strength (0-1)
minDistance	               Corners ke beech minimum distance
blockSize	               Window size for calculating intensity change
useHarrisDetector	       True → Harris, False → Shi-Tomasi
k	                       Harris free parameter (ignore for Shi-Tomasi)

🔹 5. Kaise kaam karta hai step by step
Grayscale Conversion
Color image → intensity analysis easier
Compute corner response for each window
Small W x W window scan
Intensity changes check
R = min(eigenvalues)
Threshold & Selection
Strongest corners select karo (qualityLevel se)
Corners ke beech minDistance maintain karo
Return & Draw
Coordinates integer mein convert
cv2.circle() se draw karo

🔹 6. Example Flow
Chessboard ya corner image lo → grayscale
goodFeaturesToTrack() se corners detect
Draw green/red circle
Corners visible, trackable, top N strongest

🔹 7. Practical Notes
maxCorners → jitne chahiye utne
qualityLevel → kam → zyada corners, zyada → sirf strong
minDistance → corners close ya widely spaced
Shi-Tomasi vs Harris → Shi-Tomasi stable aur faster

🔹 8. Summary in simple words
Shi-Tomasi algorithm ek window-based corner detector hai jo:
Har window ka intensity change dekhta hai
Eigenvalues se corner strength calculate karta hai
Strongest points ko select karke return karta hai
Corners ko visualize karne ke liye circles draw karte hain
'''



import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1️⃣ Image load karo (path apni image ka dena)
img = cv2.imread('shapes.png')  # apni image path set karo

if img is None:
    print("❌ Image load nahi hui, path check karo")
    exit()

# 2️⃣ Grayscale conversion
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3️⃣ Shi-Tomasi Corner Detection
corners = cv2.goodFeaturesToTrack(
    gray_img,
    maxCorners=100,       # maximum corners detect karne hain
    qualityLevel=0.01,    # chota value → weak corners bhi allow
    minDistance=10        # corners ke beech minimum distance
)

# 4️⃣ Agar corners mil gaye to draw karo
if corners is not None:
    corners = np.int32(corners)  # float → integer
    for i in corners:
        x, y = i.ravel()        # (x, y) extract
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)  # Red filled circle
else:
    print("⚠️ Koi corner detect nahi hua")

# 5️⃣ Show result using Matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(6,6))
plt.imshow(img_rgb)
plt.title('Shi-Tomasi Corner Detection')
plt.axis('off')
plt.show()


'''
Notes / Tips:
maxCorners: Jitne corners chahiye woh set karo (example: 50, 100).
qualityLevel: 0.01 → weak corners bhi detect; 0.1 → sirf strong corners.
minDistance: Do corners ke beech distance; small → corners close, large → widely spaced.
Red circle: (0,0,255) → BGR format me red.
'''
