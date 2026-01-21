'''Image Normalization 
Normalization ka matlab hai:
Image ke pixel values ko ek standard range me la dena, jaise 0 se 255.
0 → Black
255 → White
Beech ke values → Gray shades

🔹 Why normalize?
Contrast improve hota hai → Image zyada clear dikhti hai
Algorithm-friendly → ML/Computer vision me better results
Standardization → Alag images ko same scale me la sakte hain

🔹 OpenCV me normalize ka syntax
cv2.normalize(src, dst, alpha, beta, norm_type)

src → Original image
dst → Output (agar None diya → nayi image banegi)
alpha → Minimum value (usually 0)
beta → Maximum value (usually 255)
norm_type → Normalization type (common: cv2.NORM_MINMAX)
'''
# 1️⃣ Grayscale Image Normalization
import cv2

# 1. Read grayscale image
image = cv2.imread('kl.png', cv2.IMREAD_GRAYSCALE)

# 2. Normalize
normalized_image = cv2.normalize(
    image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
'''
Image 0-255 range me normalize ho jati hai
Contrast improve ho jata hai
Simple & fast'''

# 3. Show images
cv2.imshow('Original Image', image)
cv2.imshow('Normalized Image', normalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2️⃣ Color Image Normalization

# 1. Read color image
image = cv2.imread('kl.png')

# 2. Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 3. Normalize grayscale
normalized_gray_image = cv2.normalize(
    gray_image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

# 4. Convert back to color
normalized_color_image = cv2.cvtColor(
    normalized_gray_image, cv2.COLOR_GRAY2BGR)

# 5. Show images
cv2.imshow('Original Image', image)
cv2.imshow('Normalized Image', normalized_color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
Pehle color → grayscale
Phir grayscale normalize
Usko back to color convert kar diya → original image ke saath compare karne ke liye'''
