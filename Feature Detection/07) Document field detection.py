'''🔹 Template Matching kya hota hai?

Template Matching ek image processing technique hai jisme hum:

Choti image (template) ko

Bari image (document) ke andar

match karte hain

Matlab:

“Ye choti si image bari image ke kis hissay me maujood hai?”

📌 Ye technique tab use hoti hai jab:

Document ka layout fixed ho

Fields (Address, Policy No etc.) same jagah par hoti hon

🔹 Is project ka goal kya hai?

📄 Document image me se automatically:

Address field

Previous policy number field
jese specific fields detect karna aur

Unke around bounding box draw karna

🔹 Overall Solution Idea

1️⃣ Document se field ka chota hissa crop karo
2️⃣ Us cropped image ko template banao
3️⃣ Template ko poore document par match karo
4️⃣ Jahan match mile, rectangle draw karo
5️⃣ Field ka naam likh do

🔹 Approach (Simple Steps)
✅ Step 1: Field Templates banana

Document se:

Address ka chota image crop karo

Policy number ka chota image crop karo

Ye images:

doc_address.png
doc_prev_policy.png

✅ Step 2: Threshold define karna
field_threshold = {
    "prev_policy_no": 0.7,
    "address": 0.6
}


📌 Threshold ka matlab:

0.7 → 70% similarity chahiye

Higher threshold = zyada strict matching

Lower threshold = zyada matches (false bhi ho sakte hain)

🔹 Libraries ka role
import numpy as np
import imutils
import cv2


cv2 (OpenCV) → Image processing

numpy → Array operations

imutils → Image utilities (yahan optional)

🔹 Core Function: getBoxed()

Ye function:

Template match karta hai

Bounding box draw karta hai

Field ka naam likhta hai

🔸 Function parameters
def getBoxed(img, img_gray, template, field_name="policy_no"):

Parameter	Matlab
img	Original color image
img_gray	Gray scale image
template	Cropped field image
field_name	Field ka naam
🔸 Template ka size lena
w, h = template.shape[::-1]


📌 Rectangle draw karne ke liye:

width = w

height = h

🔸 Template Matching apply karna
res = cv2.matchTemplate(
    img_gray,
    template,
    cv2.TM_CCOEFF_NORMED
)


📌 TM_CCOEFF_NORMED:

Result -1 se +1 ke beech hota hai

1 ke qareeb = best match

🔸 Threshold se matches nikalna
hits = np.where(res >= field_threshold[field_name])


Yani:

Jahan similarity threshold se zyada ho, wahan hit hai

🔸 Bounding box draw karna
for pt in zip(*hits[::-1]):
    cv2.rectangle(
        img,
        pt,
        (pt[0] + w, pt[1] + h),
        (0, 255, 255),
        2
    )


📌 Yellow rectangle:

Start → pt

End → (pt[0] + w, pt[1] + h)

🔸 Field ka naam likhna
cv2.putText(
    img,
    field_name,
    (pt[0], y),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (0, 0, 255),
    1
)


📌 Red text me:

Address

prev_policy_no

🔹 Main Driver Code
🔸 Document image read karna
img = cv2.imread('doc.png')

🔸 Color → Gray conversion
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


📌 Gray image:

Faster processing

Better matching

🔸 Templates load karna
template_add = cv2.imread('doc_address.png', 0)
template_prev = cv2.imread('doc_prev_policy.png', 0)

🔸 Fields detect karna
img = getBoxed(img, img_gray, template_add, 'address')
img = getBoxed(img, img_gray, template_prev, 'prev_policy_no')

🔸 Result show karna
cv2.imshow('Detected', img)

🔹 Output kya milta hai?

📌 Document image jisme:

Address field detect

Policy number field detect

Har field ke around bounding box

Field ka label

✅ Advantages of Template Matching

✔ Computationally cheap
✔ Deep learning ki zarurat nahi
✔ Chhota dataset ho tab best
✔ Easy to implement
✔ Rule-based system ke liye acha

❌ Disadvantages

❌ Layout change ho to fail
❌ Scale / rotation handle nahi karta
❌ Overlapping fields me issue
❌ Accuracy deep learning se kam

🔹 Kab use karein?

✔ Insurance forms
✔ Bank documents (fixed format)
✔ ID cards
✔ Admission forms
✔ Invoice (same layout)


🔹 Deep Learning se comparison

| Template Matching | Deep Learning   |
| ----------------- | --------------- |
| Fast              | Slow training   |
| No dataset        | Large dataset   |
| Fixed layout      | Flexible layout |
| Simple            | Complex         |



'''

# importing libraries
import numpy as np
import imutils
import cv2

field_threshold = { "prev_policy_no" : 0.7,
                    "address"        : 0.6,
                  }

# Function to Generate bounding
# boxes around detected fields
def getBoxed(img, img_gray, template, field_name = "policy_no"):

    w, h = template.shape[::-1] 

    # Apply template matching
    res = cv2.matchTemplate(img_gray, template,
                           cv2.TM_CCOEFF_NORMED)

    hits = np.where(res >= field_threshold[field_name])

    # Draw a rectangle around the matched region. 
    for pt in zip(*hits[::-1]): 
        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h),
                                    (0, 255, 255), 2)

        y = pt[1] - 10 if pt[1] - 10 > 10 else pt[1] + h + 20

        cv2.putText(img, field_name, (pt[0], y),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1)

    return img


# Driver Function
if __name__ == '__main__':

    # Read the original document image
    img = cv2.imread('document.png')
      
    # 3-d to 2-d conversion
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     
    # Field templates
    template_add = cv2.imread('doc_address.png', 0)
    template_prev = cv2.imread('doc_prev_policy.png', 0)

    img = getBoxed(img.copy(), img_gray.copy(),
                       template_add, 'address')

    img = getBoxed(img.copy(), img_gray.copy(),
                   template_prev, 'prev_policy_no')

    cv2.imshow('Detected', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()