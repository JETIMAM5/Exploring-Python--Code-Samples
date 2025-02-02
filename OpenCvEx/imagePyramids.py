import cv2
import numpy as np

img = cv2.imread("lena.jpg")
layer = img.copy()
gp = [layer] # gp is the Gaussian Pyramid

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    # cv2.imshow(str(i), layer)

# lr1 = cv2.pyrDown(img) # pyrDown is a function that reduces the resolution of the image
# lr2 = cv2.pyrDown(lr1)
# hr = cv2.pyrUp(lr2) # pyrUp is a function that increases the resolution of the image

layer = gp[5]
cv2.imshow("Upper Level Gaussian Pyramid", layer)

lp = [layer] # lp is the Laplacian Pyramid

for i in range((5,0,-1)):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)

cv2.imshow("Original Image", img)
# cv2.imshow("pyrDown1 Image", lr1) # pyrDown1 is the first level of the pyramid
# cv2.imshow("pyrDown2 Image", lr2) # pyrDown2 is the second level of the pyramid
cv2.waitKey(0)
cv2.destroyAllWindows()
