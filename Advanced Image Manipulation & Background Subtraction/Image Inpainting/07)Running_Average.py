'''

Background Subtraction in an Image using Concept of Running Average

Background Subtraction:
Ye technique moving objects (foreground) ko static background se alag karti hai.
Example: Security camera me yard ka scene → house, trees, road = background, moving car/people = foreground

Running Average Method:
Running Average ek dynamic background model banata hai jo har frame ke sath update hota hai.

Formula:
dst(x,y)=(1−α)⋅dst(x,y)+α⋅src(x,y)

Explanation in simple words:
dst(x,y) = background model (humari current "mental picture" of background)
src(x,y) = current frame jo abhi capture hua
alpha = learning rate → kitni quickly background update hota hai

Idea:
Agar alpha chhota hai → background slowly update hota hai, temporary motion ignore hota hai
Agar alpha bada hai → background fast update hota hai, useful agar background frequently change ho

Analogy:
Socho aap apni backyard ki photo bar bar dekh rahe ho
Ek moving cat hai → running average slowly cat ko fade karta hai
Trees aur walls static rahte hain → background me clearly dikhenge

2️⃣ Flow / Logic
Step by step logic running average ke liye:
Video capture: Camera se continuous frames capture karte hain
Initialize background model: First frame ko float type me store karte hain
Update background: Har new frame ke sath cv2.accumulateWeighted() call karte hain

Display result:
Current frame = original video
Running average = estimated background
Repeat: Har frame ke sath step 3–4 repeat karo
Exit: User Esc press kare to loop break ho jaye
'''

import cv2
import numpy as np

# Step 1: Webcam start
cap = cv2.VideoCapture(0)  # 0 = default webcam

# Step 2: First frame read karo aur float me convert karo
ret, frame = cap.read()
background_model = np.float32(frame)  # Float type background

while True:
    # Step 3: Next frame capture
    ret, frame = cap.read()
    if not ret:
        break  # Agar webcam fail ho jaye

    # Step 4: Update background model
    alpha = 0.02  # Learning rate
    cv2.accumulateWeighted(frame, background_model, alpha)

    # Step 5: Convert background model back to 8-bit image for display
    background_display = cv2.convertScaleAbs(background_model)

    # Step 6: Display original frame and running average background
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Background (Running Average)', background_display)

    # Step 7: Exit on 'Esc' key
    if cv2.waitKey(30) & 0xFF == 27:
        break

# Step 8: Cleanup
cap.release()
cv2.destroyAllWindows()

'''
How it Works Visually

Frame 1: Background initialized (first frame)
Frame 2–10: Background slowly adjust hota hai → moving objects fade ho jate hain
Result: Moving object mask automatically highlight ho jata hai (foreground)

Example:
Hand camera ke samne → background partially blocked
Quick waving hand → hand gradually fade, background emphasize hota hai

5️⃣ Important Points / Tips
alpha = learning rate
Small → stable background
Large → quickly changing background
np.float32() → background model ko float type me convert karna zaruri hai
cv2.accumulateWeighted() → core function for running average
cv2.convertScaleAbs() → float background → displayable 8-bit image
Useful for: motion detection, object tracking, surveillance
'''
