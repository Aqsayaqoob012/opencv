'''
1️⃣ Background Subtraction 
Background Subtraction ek computer vision technique hai jo video me moving objects (foreground) ko static background se alag karta hai.

Example:
CCTV footage me sirf chalne wale log ya gaadiyan detect karna, walls aur parked vehicles ignore karna.
Output usually binary mask hota hai:
White pixels (255) → moving objects
Black pixels (0) → background

2️⃣ Use Cases
Pedestrian tracking – logon ko detect aur count karna
Vehicle counting – traffic monitor karna
Security – intrusions detect karna
Visitor counting – enter/exit track karna
Note: Shadows bhi move karte hain aur kabhi algorithm unko foreground samajh leta hai.

3️⃣ Popular Algorithms in OpenCV
BackgroundSubtractorMOG → Gaussian mixture-based model
BackgroundSubtractorMOG2 → Improved version, better shadow handling
Geometric Multigrid → Statistical + per-pixel Bayesian segmentation
Hum example me MOG2 use karenge kyunki ye shadows handle karta hai.
'''

import numpy as np
import cv2

# Step 1: Video load karo
cap = cv2.VideoCapture('video.mp4')  # apni video ka path yahan

# Step 2: Background subtractor create karo
fgbg = cv2.createBackgroundSubtractorMOG2()  # MOG2 handles shadows

while True:
    # Step 3: Frame read karo
    ret, frame = cap.read()
    if not ret:
        break  # Stop agar video khatam ho jaye

    # Step 4: Background subtraction apply karo
    fgmask = fgbg.apply(frame)  # binary mask generate

    # Step 5: Original aur mask dikhaye
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Foreground Mask', fgmask)

    # Step 6: Press 'Esc' to exit
    if cv2.waitKey(30) & 0xFF == 27:
        break

# Step 7: Release resources
cap.release()
cv2.destroyAllWindows()


'''
Step by Step Explanation (Roman Urdu)
cv2.VideoCapture() → Video file open karna
cv2.createBackgroundSubtractorMOG2() → Background subtraction model create karna
fgbg.apply(frame) → Background subtract karke binary foreground mask return karta hai
cv2.imshow() → Original frame aur foreground mask real-time dikhata hai
Loop tab tak chalta hai jab tak video khatam na ho ya user Esc press na kare

🔑 Notes
MOG2 shadow handling improve karta hai
Output mask me moving object white aur background black hota hai
Ye real-time applications ke liye fast aur useful hai
'''