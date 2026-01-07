'''
Adaptive Thresholding kya hai?
Simple thresholding mein ek hi threshold poori image par apply hota hai
Adaptive thresholding mein threshold har chhoti region ke liye alag calculate hota hai
Ye uneven lighting / brightness change wale images ke liye perfect hai
Matlab: Image ke bright aur dark areas ko individually threshold karna

cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)
199 → blockSize (local region = 199×199 pixels)
5 → constant subtracted from mean
'''
import cv2
image = cv2.imread('output.jpg')
img = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

thresh1 = cv2.adaptiveThreshold(img , 255 ,cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY, 199, 5)
thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY, 199, 5)

cv2.imshow('Adaptive Mean', thresh1)
cv2.imshow('Adaptive Gaussian', thresh2)



if cv2.waitKey(0) & 0xff == ord('q'):
    cv2.destroyAllWindows()