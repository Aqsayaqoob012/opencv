'''
Inpainting karna
OpenCV me do algorithms available hain:
Fast Marching Method (FMM) → cv2.INPAINT_TELEA
Ye chhoti damages ke liye fast aur achha kaam karta hai.
Algorithm edges se start karke damage ko fill karta hai, aur nearest pixels ko zyada weight deta hai.
Navier-Stokes method → cv2.INPAINT_NS
Ye texture aur larger areas ke liye better hai.
Algorithm edges se start karke color lines propagate karta hai, aur area ki variance minimize karta hai.
'''

import cv2

# Step 1: Damaged image load karo
img = cv2.imread('cat.png')

# Step 2: Mask load karo (grayscale)
mask = cv2.imread('cat_mask.png', 0)  # 0 matlab grayscale

# Step 3: Inpainting apply karo
inpainted_img = cv2.inpaint(img, mask, 3, cv2.INPAINT_NS)

# Step 4: Result save aur display karo
cv2.imwrite('cat_inpainted.png', inpainted_img)
cv2.imshow("Inpainted Image", inpainted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
Explanation 
cv2.imread('cat_damaged.png')
Ye aapki damaged image ko load karta hai.

cv2.imread('cat_mask.png', 0)
Ye mask load karta hai.
0 ka matlab grayscale hai (black & white).
cv2.inpaint(img, mask, 3, cv2.INPAINT_NS)
img → damaged image
mask → white areas ko repair karna hai

3 → inpainting radius, matlab neighborhood ka size
cv2.INPAINT_NS → algorithm choose karna
cv2.imwrite aur cv2.imshow
Result ko save aur screen par display karne ke liye.

Notes
cv2.INPAINT_NS → Navier-Stokes (texture aur large area ke liye)
cv2.INPAINT_TELEA → Fast Marching (chhoti scratches ya small damage ke liye)
radius (yahan 3) → jitna bada radius, utna zyada surrounding pixels consider hote hain'''