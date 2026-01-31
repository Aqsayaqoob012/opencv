# Image blurring ka matlab hai image ka smooth version create karna, jisme noise kam ho.
# OpenCV me popular methods:
#   1. cv2.GaussianBlur()   → Gaussian filter
#   2. cv2.blur()           → Average blur
#   3. cv2.medianBlur()     → Median blur (noise reduction ke liye best)
# Kernel size (k,k) jitna bada hoga, blur utna zyada hoga.
# Kernel size basically decides kitne surrounding pixels ko use karke blur calculate karna hai. 
# Zyada bada kernel → zyada blur; chhota kernel → subtle blur.
# Image blurring ya convolution me kernel ko har pixel ke upar center karke apply karte hain.
# Agar kernel odd size ka ho (3×3, 5×5), to exact center pixel clearly define hota hai.
import cv2
image = cv2.imread('01.jpg')

# Gaussian Blur 

Gaussian_Blur = cv2.GaussianBlur(image , (7,7) , 0)  # kernel size (odd) , sigma (0 = auto)

#  Median Blur
# Median of surrounding pixels, salt-and-pepper noise ke liye best
Median_Blur = cv2.medianBlur(image , 5)     # kernel size (sirf ek number, odd)

# Bilateral Blur
Bilateral_Blur = cv2.bilateralFilter(image , 9, 75, 75) # diameter ,sigmaColor , sigmaSpace
'''
1️⃣ diameter

Ye neighborhood ka size decide karta hai jahan blur calculate hota hai.
Matlab: har pixel ke kitne surrounding pixels consider honge.
Example: diameter=5 → 5×5 ke surrounding pixels blur me use honge.

2️⃣ sigmaColor

Ye decide karta hai intensity similarity ka weight.
Agar sigmaColor high → pixel intensities me difference ignore hoga → zyada blur
Agar sigmaColor low → sirf similar intensity pixels blur me consider honge → edges preserve rahenge.
💡 Simple: color similarity ka tolerance

3️⃣ sigmaSpace

Ye decide karta hai spatial distance ka weight.
Agar sigmaSpace high → door ke pixels bhi contribute karenge → blur wider area me
Agar sigmaSpace low → sirf nearby pixels contribute karenge → local blur
💡 Simple: distance ka tolerance
'''

cv2.imshow('Original Image' , image)
cv2.imshow('Gaussian Blur' , Gaussian_Blur)
cv2.imshow('Median Blur' , Median_Blur)
cv2.imshow('Bilateral Blur' , Bilateral_Blur)


if cv2.waitKey(0) & 0xff == ord('q'):
    cv2.destroyAllWindows()



