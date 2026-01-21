'''
Shearing 
Shearing ka matlab hai shape ko taira (slant / tircha) kar dena
bina uska area badlay.
Shape phisal jati hai, ghoomti nahi, bas tedhi ho jati hai.

Real life example
Socho ek bookshelf hai
Neechay ka hissa wahi rahe
Upar ka hissa right side ko slide ho jaye
Shelf tirchi lagay gi
Yehi shearing hai

Shearing me kya hota hai?
Size almost same
Area same
Angle bigar jata hai
Shape parallelogram jaisi ho jati hai
'''

'''
Types of Shearing 

1) X-Shear (Side wali shearing
Y same rehta hai
X aagay peeche slide hota hai

Formula (easy):
x new = x + (shear × y)
y new = y
Upar wala hissa zyada slide karta hai
'''
import cv2
import numpy as np

# Image load
img = cv2.imread("tomato.jpg")
rows, cols = img.shape[:2]

# Shear factor
shx = 0.5  # horizontal shear
shy = 0    # vertical shear nahi

# Shear matrix (X-Shear)
M = np.float32([[1, shx, 0],
                [shy, 1, 0]])

# Apply shear
sheared_img = cv2.warpAffine(img, M, (cols, rows))

# Show images
cv2.imshow("Original", img)
cv2.imshow("X-Sheared", sheared_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
2) Y-Shear (Upar neeche shearing)
X same rehta hai
Y upar neeche slide hota hai

Formula:
x new = x
y new = y + (shear × x)
Right side zyada move karti hai
'''

# Image load
img = cv2.imread("tomato.jpg")
rows, cols = img.shape[:2]

# Shear factor
shx = 0    # horizontal shear nahi
shy = 0.3  # vertical shear

# Shear matrix (Y-Shear)
M = np.float32([[1, shx, 0],
                [shy, 1, 0]])

# Apply shear
sheared_img = cv2.warpAffine(img, M, (cols, rows))

# Show images
cv2.imshow("Original", img)
cv2.imshow("Y-Sheared", sheared_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
3) X-Y Shear (Dono taraf)

X bhi change
Y bhi change

Ek chhota example

Point hai (1, 1)
Shear = 2

X-shear:
x new = 1 + 2×1 = 3
y new = 1
→ (3,1)

Y-shear:
x new = 1
y new = 1 + 2×1 = 3
→ (1,3)
'''


# Image load
img = cv2.imread("tomato.jpg")
rows, cols = img.shape[:2]

# Shear factors
shx = 0.5  # horizontal
shy = 0.3  # vertical

# Shear matrix (X-Y Shear)
M = np.float32([[1, shx, 0],
                [shy, 1, 0]])

# Apply shear
sheared_img = cv2.warpAffine(img, M, (cols, rows))

# Show images
cv2.imshow("Original", img)
cv2.imshow("X-Y Sheared", sheared_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
