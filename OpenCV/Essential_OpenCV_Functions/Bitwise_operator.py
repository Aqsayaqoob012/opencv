# Bitwise AND pixel-by-pixel logical AND operation karta hai.
# Sirf woh area show hota hai jo dono images mein common ho

import cv2
image1 = cv2.imread('square.png')
image2 = cv2.imread('circle.png')

# Bitwise AND pixel-by-pixel logical AND operation karta hai.
# Sirf woh area show hota hai jo dono images mein common ho
BWA = cv2.bitwise_and(image1 , image2  , mask=None ) # mask=None Operation poori image par apply hota hai , Koi specific area restrict nahi hota 

# Jab aap dono images ka content combine karna chahte ho.
# Square + Circle dono show honge
BWO = cv2.bitwise_or(image1 , image2  , mask=None )

# Jab aap sirf different (non-common) areas dikhana chahte ho.
# Sirf unique parts visible
BWXOR = cv2.bitwise_xor(image1 , image2  , mask=None )

# Jab aap image invert karna chahte ho.
BWN1 = cv2.bitwise_not(image1 , mask=None)
BWN2 = cv2.bitwise_not(image2 , mask=None)

cv2.imshow('Bitwise Operaotr' , BWA)
cv2.imshow('Bitwise Operaotr' , BWO)
cv2.imshow('Bitwise Operaotr' , BWXOR)
cv2.imshow('Bitwise Operaotr' , BWN1)
cv2.imshow('Bitwise Operaotr' , BWN2)

if cv2.waitKey(0) & 0xff == ord('q'):
    print('Quitting...')
    cv2.destroyAllWindows()  