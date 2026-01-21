'''
Image Pyramid 
Image pyramid ek stack of images hai, jisme same image different sizes me hoti hai.
Top level → smallest image
Bottom level → original image

🔹 Why use?
Memory save → chhoti images pe fast processing
Object detection → different sizes objects detect karna
Image blending → smooth blending of images
Edge detection → multiple resolutions se edges detect karna
'''
'''
1️⃣ Pyramid Down (cv2.pyrDown)
Idea: Image ko chhota karo
Size → half (width & height)
Gaussian blur automatically lagta hai
✅ Output → Half size + slightly blurred
'''

import cv2

img = cv2.imread("pyramid_sample.jpg")

downsampled = cv2.pyrDown(img)

cv2.imshow("Original", img)
cv2.imshow("Downsampled", downsampled)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
2️⃣ Pyramid Up (cv2.pyrUp)
Idea: Image ko bada karo
Size → double (width & height)
Gaussian blur lagta hai smoothness ke liye
✅ Output → Double size, thoda blurred
'''
import cv2

img = cv2.imread("pyramid_sample.jpg")

upsampled = cv2.pyrUp(img)

cv2.imshow("Original", img)
cv2.imshow("Upsampled", upsampled)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''
3️⃣ Gaussian Pyramid (Multiple Levels)
Idea: Multiple levels bana ke image ko smallest → original tak show karo

✅ Output →
Level 0 → Original
Level 1 → Half size
Level 2 → Quarter size
Level 3 → Eighth size
'''

import cv2

img = cv2.imread("pyramid_sample.jpg")

pyramid = [img]

# 3 levels of downsampling
for i in range(3):
    img = cv2.pyrDown(img)
    pyramid.append(img)

# Display from smallest → original
for i in range(len(pyramid)-1, -1, -1):
    print(f"Pyramid Level {i}")
    cv2.imshow(f"Level {i}", pyramid[i])
    cv2.waitKey(0)

cv2.destroyAllWindows()
