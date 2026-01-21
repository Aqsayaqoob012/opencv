'''
🔹 cv2.copyMakeBorder() kya karta hai? (Easy words)
Image ke chaaron taraf border/padding add karta hai

Useful:
Image ko frame dena
Machine learning ke liye same size images banana
Image ka focus/feature highlight karna

🔹 Syntax
cv2.copyMakeBorder(src, top, bottom, left, right, borderType, value)

Parameter	Meaning
src	        Original image
top	Top     border size (pixels)
bottom	    Bottom border size
left	    Left border size
right	    Right border size
borderType	Type of border (BORDER_CONSTANT, BORDER_REFLECT, etc.)
value	    Color of border (only for BORDER_CONSTANT)

🔹 Border Types
Type	Effect
BORDER_CONSTANT	Solid color border (value se set karo)
BORDER_REFLECT	Mirror reflection of edge pixels
BORDER_REFLECT_101	Like reflect but slight change at edge
BORDER_REPLICATE	Outer pixels repeated

'''
#🔹 Example 1: Constant Border (Black)
# ✅ Output → Image ke chaaron taraf black border
import cv2

img = cv2.imread("tomato.jpg")

# Add 10px black border all sides
bordered = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=0)

cv2.imshow("Bordered Image", bordered)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 🔹 Example 2: Constant Border (Custom Color)
# ✅ Output → Red border around image
import cv2

img = cv2.imread("tomato.jpg")

# Add 10px **red** border
bordered_red = cv2.copyMakeBorder(img, 10, 10, 10, 10,
                                  cv2.BORDER_CONSTANT, value=(0, 0, 255))

cv2.imshow("Red Border", bordered_red)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Example 3: Reflect / Replicate Borders
#✅ Output → Reflect → Edge mirrored , Reflect_101 → Slightly different mirrored , Replicate → Outer pixels repeat

import cv2

img = cv2.imread("tomato.jpg")

reflect = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_REFLECT)
reflect_101 = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_REFLECT_101)
replicate = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_REPLICATE)

cv2.imshow("Reflect", reflect)
cv2.imshow("Reflect_101", reflect_101)
cv2.imshow("Replicate", replicate)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''
Use Cases
Machine learning preprocessing → input images same size
Highlight object → border se object stand out
Display/Visualization → frames ya borders for clarity'''