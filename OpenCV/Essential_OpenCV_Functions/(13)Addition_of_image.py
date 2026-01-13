import cv2
image1 = cv2.imread('1.jpg')
image2 = cv2.imread('new_image.jpg')
'''
Parameters:
image1 → first image
0.5 → first image ka weight (50%)
image2 → second image
0.4 → second image ka weight (40%)
0 → gamma (brightness adjust, normally 0)

Result = (image1 * alpha) + (image2 * beta) + gamma

'''
weightedSum = cv2.addWeighted(image1 , 0.5 , image2 , 0.4 , 0)
cv2.imshow('original Image 1', image1)
cv2.imshow('original Image 2', image2)
cv2.imshow('Weighted Image', weightedSum)
cv2.waitKey(0)
cv2.destroyAllWindows()

if cv2.waitKey(1) & 0xff == ord('q'):
    print('Quitting...')
    cv2.destroyAllWindows()
