import cv2
import numpy as np

img = cv2.imread("lena.jpg", cv2.IMREAD_COLOR)

px = img[55,55]  # [94,123,227]
# print(px) # Actual color of the pixel
px = [255,255,255] # Changing the color of the pixel or img[55,55] = [255,255,255] is also valid
print(px) # now the color of the pixel is white [255,255,255]

# ROI: Region of Image
roi = img[100:150, 100:150] = [255,255,255] # Changing the color of the region of the image

lena_face = img[220:370, 235:355]
img[0:150, 0:120] = lena_face

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()