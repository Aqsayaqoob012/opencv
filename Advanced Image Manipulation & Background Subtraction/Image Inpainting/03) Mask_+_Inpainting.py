'''
Mask + Inpainting combine karna
Ek hi script me mask create + inpainting:
'''

import cv2
import numpy as np

# Damaged image load
img = cv2.imread('cat.png')

# Automatic mask
mask = np.zeros_like(img)
mask[np.sum(img, axis=2) == 0] = 255

# Grayscale me convert
mask_gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
cv2.imwrite('cat_mask.png', mask_gray)

# Inpaint
inpainted = cv2.inpaint(img, mask_gray, 3, cv2.INPAINT_NS)

# Save aur display
cv2.imwrite('cat_inpainted.png', inpainted)
cv2.imshow("Inpainted", inpainted)
cv2.waitKey(0)
cv2.destroyAllWindows()
