import cv2
import numpy as np


# ----------------------------------------- ADD TWO IMAGES -----------------------------------------
# img1 =  cv2.imread("3D-Matplotlib.png")
# img2 =  cv2.imread("mainsvmimage.png")
# #add = img1 + img2 # but this addition
# # (155, 211, 79) + (50, 170, 200) = 205, 381, 279...translated to (205, 255, 255) because of the limit of 255
# add = cv2.add(img1,img2) # adds the pixel values of the two images together

# weighted =  cv2.addWeighted(img1, 0.6, img2, 0.4, 0) # 0.6 and 0.4 are the weights of the images
# cv2.imshow("weighted", weighted)
# --------------------------------------------------------------------------------------------------

# ---------------------------------------- THRESHOLDING --------------------------------------------
img1 =  cv2.imread("3D-Matplotlib.png")
img2 =  cv2.imread("mainlogo.png")

rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV) # 220 is the threshold value

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow("res", img1)
# # cv2.imshow("mask_inv",mask_inv)
# # cv2.imshow("img1_bg",img1_bg)
# # cv2.imshow("img2_fg",img2_fg)
# # cv2.imshow("dst",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.imshow("mask",mask)

# --------------------------------------------------------------------------------------------------
