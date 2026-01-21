'''
* Grayscaling

Grayscaling ka matlab hai color image (RGB/BGR) ko black se white ke shades me convert karna.Black = 0
White = 255
Beech ke shades = gray

Grayscale image me sirf 1 channel hota hai
Color image me 3 channels (B, G, R) hotay hain

* Grayscale kyun important hai?
1. Fewer dimensions
RGB → 3 channels
Grayscale → 1 channel
Processing fast ho jati hai

2. Simpler models
Data kam → ML/DL models fast train hotay hain

3. Algorithm-ready
Kuch algorithms sirf grayscale pe kaam kartay hain
Canny Edge Detection
Thresholding
Morphological operations
'''

'''
Method 1: cv2.cvtColor()
Sab se best & recommended method
Kaam kaisay karta hai?
OpenCV internally weighted formula use karta hai
Result ek single-channel grayscale image hota hai
'''
import cv2

img = cv2.imread("tomato.jpg")   # Color image (BGR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Grayscale", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
Method 2: cv2.imread(path, 0)
Direct grayscale load karna
Kaam kaisay karta hai?
Image load hotay hi OpenCV usko grayscale bana deta hai
Conversion alag se nahi karni parti
'''


gray = cv2.imread("tomato.jpg", 0)  # 0 = grayscale

cv2.imshow("Grayscale Image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''Method 3.1: Weighted Method (Recommended manually)
Formula:
grey = 0.2989R + 0.5870G + 0.1140B

Ye weights kyun?

Human eye:

Green → zyada sensitive
Red → medium
Blue → kam

Kaam kaisay karta hai?
Har pixel pe loop lagta hai
BGR values se brightness calculate hoti hai
Same value 3 channels me daal di jati hai
Result visually realistic hota hai
Lekin slow hota hai (Python loops ki wajah se)
'''


img = cv2.imread("tomato.jpg")
rows, cols = img.shape[:2]

for i in range(rows):
    for j in range(cols):
        B = img[i, j][0]
        G = img[i, j][1]
        R = img[i, j][2]

        gray = 0.2989*R + 0.5870*G + 0.1140*B
        img[i, j] = [gray, gray, gray]

cv2.imshow("Weighted Grayscale", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
Method 3.2: Average Method
Formula:
      Gray=(R+G+B)/3
Kaam kaisay karta hai?
Teenon channels ko equal weight deta hai
Simple average nikalta hai

Problem:
Human eye ko follow nahi karta
Image thori flat / dull lagti hai
Slow (pixel by pixel loop)'''




img = cv2.imread("tomato.jpg")
rows, cols = img.shape[:2]

for i in range(rows):
    for j in range(cols):
        B, G, R = img[i, j]
        gray = (int(B) + int(G) + int(R)) / 3
        img[i, j] = [gray, gray, gray]

cv2.imshow("Average Grayscale", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
