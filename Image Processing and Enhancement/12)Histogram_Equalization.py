'''🔹 Histogram Equalization kya hai? (Easy words)
Image ke contrast ko improve karne ka technique
Dark aur bright areas ko evenly spread karta hai
Hidden details visible ho jate hain
Example: Agar image bohot dark ya bohot bright hai → HE se details clear ho jati hain

🔹 Kaise kaam karta hai?
Histogram calculate → pixel intensity frequency
CDF calculate → cumulative distribution function
CDF normalize → pixel values ko 0–255 range me map
Apply transformation → new pixel values → improved contrast'''

'''
1️⃣ Grayscale image HE
✅ Output → Left: Original, Right: Equalized
Brightness & contrast improve ho jati hai
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Load grayscale image
img = cv2.imread('koala_sample.jpg', 0)  # 0 means grayscale

# 2. Apply histogram equalization
equ = cv2.equalizeHist(img)

# 3. Stack images side by side
res = np.hstack((img, equ))

# 4. Show result
plt.figure(figsize=(10, 5))
plt.imshow(res, cmap='gray')
plt.title("Original vs Equalized Image")
plt.axis('off')
plt.show()

'''
2️⃣ Color Image HE (per channel)

OpenCV ka cv2.equalizeHist() sirf grayscale me kaam karta hai,
 lekin hum color image ke RGB channels ko alag-alag equalize kar sakte hain
 ✅ Output → Color image ke brightness/contrast improve ho jati hai, colors natural rehte hain'''



# Convert to YCrCb color space (luminance channel equalize karna easy)
ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

# Equalize the Y channel (brightness)
ycrcb[:,:,0] = cv2.equalizeHist(ycrcb[:,:,0])

# Convert back to BGR
result = cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)

# Show result
cv2.imshow("Original", img)
cv2.imshow("Equalized", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
🔹 Real-Life Applications
Medical Imaging: X-ray, CT scan ke contrast improve
Satellite/Aerial images: Terrain visibility better
Surveillance: Low-light video enhance

🔹 Limitations
Noise Amplification → noisy image me aur noise badh jata hai
Over-enhancement → kabhi image unnatural lag sakti hai
Solution: Use CLAHE (Contrast Limited Adaptive Histogram Equalization)'''