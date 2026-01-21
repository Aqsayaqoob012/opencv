
# Image blurring ka matlab hai image ka smooth version create karna, jisme noise kam ho.
# OpenCV me popular methods:
#   1. cv2.GaussianBlur()   → Gaussian filter
#        Image ko smooth / blur karta hai lekin edges ko thora better preserve karta hai.
#        Har pixel ke around Gaussian distribution (bell curve) use karta hai
#        Center pixel ko zyada weight deta hai
#        Door walay pixels ko kam weight
#          Is liye blur natural lagta hai.

#   2. cv2.blur()           → Average blur
#Image ko simple average se blur karta hai.
#      Kernel ke andar jitnay pixels hain
#      Sab ka average nikalta hai
#      Center pixel ko replace kar deta hai
#      Sab pixels ko equal weight milta ha 
# Kab use hota hai? => Simple blur , Fast processing ,  Jab quality zyada important na ho

#   3. cv2.medianBlur()     → Median blur (noise reduction ke liye best)
# Kernel size (k,k) jitna bada hoga, blur utna zyada hoga.
 #        Image se salt & pepper noise remove karta hai.
 #        Kernel ke andar pixels ko sort karta hai
 #        Middle (median) value pick karta hai
 #        Usko center pixel bana deta hai
 #        Is liye edges distort nahi hotay
# Kab use hota hai? => Black & white dots noise , Text / documents ,Face images


# Salt & Pepper noise ka matlab hota hai image me random white aur black dots ka aa jana.
# Kuch pixels bilkul white (255) ho jatay hain
# Kuch pixels bilkul black (0) ho jatay hain
# Baqi image normal rehti hai
# Image aisi lagti hai jaisay purani TV screen ho.

# Kernel (jisko filter / mask / matrix bhi kehtay hain) ek chhoti si matrix hoti hai
#  jo image par slide hoti hai aur har pixel par calculation karti hai.

import cv2

image = cv2.imread('01.jpg')

# Gaussian Blur 

Gaussian_Blur = cv2.GaussianBlur(image , (7,7) , 0)  # kernel size (odd) , sigma (0 = auto)

#  Median Blur
# Median of surrounding pixels, salt-and-pepper noise ke liye best
Median_Blur = cv2.medianBlur(image , 5)     # kernel size (sirf ek number, odd)

# Bilateral Blur
Bilateral_Blur = cv2.bilateralFilter(image , 9, 75, 75) # diameter ,sigmaColor , sigmaSpace

cv2.imshow('Original Image' , image)
cv2.imshow('Gaussian Blur' , Gaussian_Blur)
cv2.imshow('Median Blur' , Median_Blur)
cv2.imshow('Bilateral Blur' , Bilateral_Blur)


if cv2.waitKey(0) & 0xff == ord('q'):
    cv2.destroyAllWindows()