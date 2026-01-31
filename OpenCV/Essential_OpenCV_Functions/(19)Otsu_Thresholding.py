'''
Otsu Thresholding – Simple Explanation
Otsu thresholding me threshold value hum khud choose nahi kartay.
OpenCV image ke histogram ko analyze karta hai aur automatically best threshold nikalta hai.

Key Idea
Image bimodal honi chahiye
(yaani histogram me 2 peaks: background + object)
Otsu algorithm aisi threshold value choose karta hai:
jo foreground aur background ka variance minimum kar de

Threshold is chosen so that background aur foreground apni classes me maximum similar ho, 
aur dono classes ek dusre se clearly alag dikhain

✔ Otsu sirf grayscale image par kaam karta hai
❌ Color image par nahi
'''
import cv2
image = cv2.imread('output.jpg')
img = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

# cv2.threshold(image, threshold_value, max_value, method)
# Threshold value ko 0 rakhte hain, Otsu khud calculate karega
ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

print("Calculated Otsu Threshold:", ret)


cv2.imshow('Original', img)
cv2.imshow('Otsu Thresholded', thresh)



if cv2.waitKey(0) & 0xff == ord('q'):
    cv2.destroyAllWindows()