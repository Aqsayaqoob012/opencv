'''
Interactive Mask Drawing using Mouse
Agar aap mouse se manually draw karna chahte ho ki kahan inpainting karni hai ,
 to ye code use karo:'''

import cv2
import numpy as np

drawing = False  # True jab mouse press ho
ix, iy = -1, -1

# Empty mask same size as image
img = cv2.imread('cat.png')
mask = np.zeros(img.shape[:2], np.uint8)

# Mouse callback function
def draw_mask(event, x, y, flags, param):
    global ix, iy, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.circle(mask, (x, y), 5, 255, -1)
            cv2.circle(img, (x, y), 5, (0,0,255), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(mask, (x, y), 5, 255, -1)
        cv2.circle(img, (x, y), 5, (0,0,255), -1)

cv2.namedWindow('Draw Mask')
cv2.setMouseCallback('Draw Mask', draw_mask)

while True:
    cv2.imshow('Draw Mask', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:  # ESC press to exit
        break

cv2.destroyAllWindows()
cv2.imwrite('interactive_mask.png', mask)

# Inpaint using drawn mask
inpainted_img = cv2.inpaint(cv2.imread('cat_damaged.png'), mask, 3, cv2.INPAINT_NS)
cv2.imwrite('inpainted_interactive.png', inpainted_img)
cv2.imshow("Inpainted Interactive", inpainted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
Iska use:
Image open hogi aur aap mouse se red lines draw karenge.
Ye red lines automatically mask me white ho jayengi.
ESC press karne par mask save ho jayega aur inpainting ho jayegi.

'''