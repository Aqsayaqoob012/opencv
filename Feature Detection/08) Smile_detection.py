'''😊 Smile Detection using OpenCV (Theory)
🔹 Smile Detection kya hoti hai?

Smile detection ek computer vision technique hai jisme:

Camera ya image se human face detect kiya jata hai

Phir us face ke andar smile (muskurahat) ko identify kiya jata hai

📌 Ye technique use hoti hai:

Media analysis (public reaction)

Photo apps (auto capture on smile)

Attendance & emotion analysis

Human–computer interaction

🔹 Is system ka basic idea

Smile detection system 3 main steps follow karta hai:

1️⃣ Webcam se live video capture
2️⃣ Pehle face detect karna
3️⃣ Phir sirf face ke andar smile detect karna

Ye kaam Haar Cascade classifiers ki madad se hota hai.

🔹 Haar Cascade Classifier kya hota hai?

Haar Cascade ek machine learning based object detection technique hai jo:

Image me patterns detect karti hai

Jaise: eyes, nose, mouth, smile, face

📌 Ye already pre-trained hoti hai
📌 Matlab hume model train karna nahi parta

Haar cascade kaam karta hai:

Haar features

Integral image

AdaBoost

Cascade of classifiers

Is wajah se ye:
✔ Fast
✔ Lightweight
✔ Real-time ke liye suitable

🔹 Step-by-Step Theory Explanation
🟢 Step 1: OpenCV Library Import Karna
import cv2


📌 OpenCV:

Image & video processing

Object detection

Real-time computer vision tasks

Smile detection me OpenCV:

Webcam access karta hai

Haar cascade apply karta hai

Rectangles draw karta hai

🟢 Step 2: Pre-trained Haar Cascades Load Karna
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml'
)

smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_smile.xml'
)


📌 Yahan:

Face cascade → face detect karta hai

Eye cascade → aankhen detect karta hai (optional)

Smile cascade → muskurahat detect karta hai

✔ Ye files OpenCV ke sath already hoti hain
✔ Machine learning se train ki hui hoti hain

🟢 Step 3: Webcam Start Karna
cap = cv2.VideoCapture(0)


📌 0 ka matlab:

Default webcam use karo

OpenCV:

Webcam se frames (images) leta hai

Har frame ko image ki tarah process karta hai

🟢 Step 4: Har Frame ka Processing
🔸 Frame read karna
ret, frame = cap.read()


ret → True/False (frame mila ya nahi)

frame → actual image

🔸 Color se Gray me convert karna
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


📌 Haar cascades:

Sirf grayscale image pe kaam karti hain

Gray image fast hoti hai

Unnecessary color info remove ho jati hai

🔸 Face detection
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=5
)


📌 Parameters explanation:

Parameter	Matlab
scaleFactor	Image ko kitna resize karna
minNeighbors	Detection ki strictness
return	Faces ke rectangles
🔸 Face ke around rectangle draw karna
cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)


📌 Blue rectangle:

Face ka location show karta hai

🔸 Face ka ROI (Region of Interest)
roi_gray = gray[y:y+h, x:x+w]


📌 ROI ka matlab:

Sirf face ke andar search karna

✔ Speed fast
✔ False detection kam

🔸 Smile detection
smiles = smile_cascade.detectMultiScale(
    roi_gray,
    scaleFactor=1.8,
    minNeighbors=20,
    minSize=(25,25)
)


📌 Smile detect karna:

Sirf face ke andar

Mouth area ke around

📌 Green rectangle:

cv2.rectangle(frame, (x+sx, y+sy),
              (x+sx+sw, y+sy+sh),
              (0,255,0), 2)

🟢 Step 5: Result Show Karna aur Exit
cv2.imshow('Smile Detection', frame)


Real-time window:

Face + smile rectangles

Exit ke liye:

if cv2.waitKey(1) & 0xFF == ord('q'):
    break


Finally:

cap.release()
cv2.destroyAllWindows()

✅ Advantages of Smile Detection using OpenCV

✔ Real-time detection
✔ Pre-trained models (no training needed)
✔ Fast & lightweight
✔ Low hardware requirement
✔ Easy to implement for beginners

❌ Limitations

❌ Poor lighting me accuracy kam
❌ Face angle change ho to problem
❌ Glasses, beard, mask me issue
❌ Multiple faces me performance slow
❌ Emotion accuracy limited (sirf smile)

🔍 Summary (Exam Ready)

Smile detection using OpenCV ek real-time facial expression recognition system hai jo Haar Cascade classifiers ki madad se:

Pehle face detect karta hai

Phir us face ke andar smile detect karta hai

Ye system fast, simple aur beginner-friendly hai lekin complex real-world scenarios me limited accuracy deta hai.'''


import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_smile.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]

        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20, minSize=(25, 25))

        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(frame, (x + sx, y + sy), (x + sx + sw, y + sy + sh), (0, 255, 0), 2)

    cv2.imshow('Smile Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()