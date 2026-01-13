'''
Otsu Thresholding – Simple Explanation
Otsu thresholding me threshold value hum khud choose nahi kartay.
OpenCV image ke histogram ko analyze karta hai aur automatically best threshold nikalta hai.

Key Idea
Image bimodal honi chahiye
(yaani histogram me 2 peaks: background + object)
Otsu algorithm aisi threshold value choose karta hai:
jo foreground aur background ka variance minimum kar de

✔ Otsu sirf grayscale image par kaam karta hai
❌ Color image par nahi
'''
import cv2
image = cv2.imread('output.jpg')
img = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

thresh1 = cv2.Threshold(img , 255 ,cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY, 199, 5)

cv2.imshow('Adaptive Mean', thresh1)
cv2.imshow('Adaptive Gaussian', thresh2)



if cv2.waitKey(0) & 0xff == ord('q'):
    cv2.destroyAllWindows()