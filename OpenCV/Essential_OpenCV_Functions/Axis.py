import matplotlib.pyplot as plt
import cv2
image = cv2.imread('1.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(8, 6))
plt.imshow(image)

# Axis ON
plt.axis('on')

# Grid ON
plt.grid(color='white', linestyle='--', linewidth=0.5)

plt.show()