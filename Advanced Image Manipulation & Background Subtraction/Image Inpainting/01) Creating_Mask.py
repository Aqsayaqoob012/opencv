'''
1️⃣ Image Inpainting kya hai?
Image inpainting ka matlab hai image me unwanted ya damage areas ko remove karna.
Ye scratches, text, stains ya koi unwanted object ho sakta hai.
Ye algorithm damage wale pixels ko aas paas ke pixels se replace karta hai taki wo naturally blend ho jaye.
Example: Agar purani photo me scratch ho, inpainting se wo scratch remove ho jata hai aur photo clean lagti hai.

2️⃣ Mask kya hai aur kyun chahiye?
Inpainting ke liye hume ek mask chahiye, jo black-and-white image hoti hai:
White pixels (255) → ye wo area hai jo remove/inpaint karna hai.
Black pixels (0) → ye wo area hai jo unchanged rahega.
Aap manually GIMP ya Photoshop me mask bana sakte ho, lekin OpenCV se ye programmatically bhi ban sakta hai.
'''

# Mask create karna OpenCV me
# Automatic mask create karne ka simple tareeqa ye hai:
# np.sum(damaged_img, axis=2) == 0 matlab pixel bilkul black hai.
# Ye black pixels white me convert ho jate hain mask ke liye.

import cv2
import numpy as np

# Damaged image load karo
damaged_img = cv2.imread("cat.png")

# Mask create karne ke liye black pixels ko white aur baaki ko black banao
mask = np.zeros_like(damaged_img)
mask[np.sum(damaged_img, axis=2) == 0] = 255  # black pixels ko white bana do

# Mask ko grayscale me convert karo
mask_gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
cv2.imwrite('cat_mask.png', mask_gray)

# Mask dikhana
cv2.imshow("Mask", mask_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()