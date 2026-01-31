'''
Adaptive Thresholding kya hai?
Simple thresholding mein ek hi threshold poori image par apply hota hai
Adaptive thresholding mein threshold har chhoti region ke liye alag calculate hota hai
Ye uneven lighting / brightness change wale images ke liye perfect hai
Matlab: Image ke bright aur dark areas ko individually threshold karna

cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)
199 → blockSize (local region = 199×199 pixels)
5 → constant subtracted from mean


Example (small scale)

Assume ek 3×3 neighborhood (simpler than 199×199 for samajhne ke liye):

| 120 | 130 | 140 |
| --- | --- | --- |
| 125 | 150 | 135 |
| 110 | 145 | 155 |

Step 1: Sum all pixels
120 + 130 + 140 + 125 + 150 + 135 + 110 + 145 + 155 = 1210

Step 2: Divide by number of pixels
Number of pixels = 3×3 = 9

Average = 1210 ÷ 9 ≈ 134

Step 3: Threshold with C

Agar C = 5 → threshold = 134 − 5 = 129

Pixel P ka value > 129 → white

Pixel P ka value ≤ 129 → black

💡 Intuition:
Har pixel ka threshold alag hota hai, kyunki har pixel ka neighborhood alag ho sakta hai.

Bright region → threshold high

Dark region → threshold low
→ Isliye uneven lighting me adaptive thresholding kaam aata hai.
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


    '''
    Adaptive Thresholding ka basic idea

Adaptive thresholding me har pixel ka threshold poore image ke liye ek hi number nahi, balki us pixel ke local neighborhood ka average hota hai.

Formula (Mean method) simple version me:

Threshold at pixel
=
Mean of block
−
𝐶
Threshold at pixel=Mean of block−C

block = blockSize × blockSize pixels (tumhare case me 199×199)

C = ek constant number jo subtract hota hai threshold se

Example (numbers ke saath)

Suppose local block mean = 150

C = 0 → threshold = 150

pixel value 151 → white

pixel value 149 → black

C = 5 → threshold = 150 − 5 = 145

pixel value 146 → white (ab zyada pixels white)

pixel value 144 → black

C = -5 → threshold = 150 − (-5) = 155

pixel value 156 → white (threshold zyada → fewer pixels white)

pixel value 154 → black
    '''