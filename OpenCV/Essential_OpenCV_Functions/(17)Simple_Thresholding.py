''' Thresholding kya hai?
Thresholding ek image segmentation technique hai jisme:
Har pixel value ko ek threshold se compare kiya jata hai
Agar pixel value threshold se kam → 0 (black)
Agar pixel value threshold se zyada → 255 (white) 

f(x, y) < T → f(x, y) = 0
f(x, y) ≥ T → f(x, y) = 255
f(x, y) → pixel value at coordinate (x, y)
T → threshold value


f(x, y) = pixel value at (x, y)
T = threshold value

Agar f(x, y) < T:
    f(x, y) = 0     # black (background)

Agar f(x, y) >= T:
    f(x, y) = 255   # white (foreground)
'''
import cv2
image = cv2.imread('output.jpg')
img = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

# applying different thresholding techniques on the input image all pixels value above 120 will be set to 255
# ret, thresh = cv2.threshold(src, T, maxVal, type)

ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow('Binary Threshold', thresh1)
cv2.imshow('Binary Threshold Inverted', thresh2)
cv2.imshow('Truncated Threshold', thresh3)
cv2.imshow('Set to 0', thresh4)
cv2.imshow('Set to 0 Inverted', thresh5)


if cv2.waitKey(0) & 0xff ==  ord('q'):
    print("Quitting...")
    cv2.destroyAllWindows()