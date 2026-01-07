import cv2
image = cv2.imread('output.jpg')
img = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

thresh1 = cv2.Threshold(img , 255 ,cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY, 199, 5)

cv2.imshow('Adaptive Mean', thresh1)
cv2.imshow('Adaptive Gaussian', thresh2)



if cv2.waitKey(0) & 0xff == ord('q'):
    cv2.destroyAllWindows()