'''
1️⃣ Image Negative
Image ka photographic negative

Formula:
s = L - 1 - r
L = 256 (8-bit image), r = pixel value

✅ Output → Dark pixels bright, bright pixels dark
'''

import cv2
import numpy as np

# Read image
img = cv2.imread('tomato.jpg', cv2.IMREAD_GRAYSCALE)

# Image negative
negative = 255 - img

cv2.imshow("Original", img)
cv2.imshow("Negative", negative)


'''
2️⃣ Log Transformation
Dark pixels ko zyada highlight karo

Formula:
s = c ⋅ log ( 1 + r )
c = 255 / log(1 + max_pixel)

✅ Output → Low intensity areas zyada bright
'''



c = 255 / np.log(1 + np.max(img))
log_transformed = c * np.log(1 + img)

log_transformed = np.array(log_transformed, dtype=np.uint8)

cv2.imshow("Log Transformed", log_transformed)

'''
3️⃣ Gamma (Power-Law) Transformation
Brightness adjust karna (monitor/view ke liye)

Formula:
s = c ⋅ r (power of y)
γ > 1 → darker
γ < 1 → lighter

✅ Output → Alag-alag gamma values se image lighter/darker
'''



for gamma in [0.5, 1.2, 2.2]:
    gamma_corrected = np.array(255*(img/255)**gamma, dtype='uint8')
    cv2.imshow(f'Gamma {gamma}', gamma_corrected)



'''
4️⃣ Piecewise-Linear / Contrast Stretching
Image ka contrast enhance karna
Dark pixels thoda brighter
Bright pixels thoda zyada bright
Linear function in intervals
✅ Output → Dark regions brighter, bright regions maintain
'''


def pixelVal(pix, r1, s1, r2, s2):
    if 0 <= pix <= r1:
        return (s1/r1)*pix
    elif r1 < pix <= r2:
        return ((s2-s1)/(r2-r1))*(pix-r1)+s1
    else:
        return ((255-s2)/(255-r2))*(pix-r2)+s2

img = cv2.imread('tomato.jpg')
r1, s1 = 70, 0
r2, s2 = 140, 255

pixelVal_vec = np.vectorize(pixelVal)
contrast_stretched = pixelVal_vec(img, r1, s1, r2, s2)

cv2.imshow("Contrast Stretched", contrast_stretched.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
| Transformation   | Effect                                       |
| ---------------- | -------------------------------------------- |
| Negative         | Dark ↔ Bright swap                           |
| Log              | Dark pixels brighten                         |
| Gamma            | Brightness control (γ>1 darker, γ<1 lighter) |
| Contrast Stretch | Enhance contrast (dark→light, bright→bright) |
'''