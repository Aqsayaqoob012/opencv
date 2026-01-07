import cv2

cap = cv2.VideoCapture(0)

while True:
  ret , frame = cap.read()  # ret = > True / False  , frame => image
  
  if not ret:
    print('Could not read Frame')
    break
  cv2.imshow("Camera Feed", frame)

  if cv2.waitKey(1) & 0xFF  == ord('q'): # wait for 1 mili second ( agr koi key press nahi ki jati tu -1 return kry ga wrna q ka ASSCI code ay ga)
   print('quitting...')
   break
cap.release()  
cv2.destroyAllWindows()

