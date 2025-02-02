import numpy as np 
import matplotlib.pyplot as plt 
import cv2


img = cv2.imread("smarties.png", cv2.IMREAD_GRAYSCALE)
# _, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((2,2), np.uint8)

dilation = cv2.dilate(img, kernel, iterations=5) # dilation is that it adds pixels to the boundaries of objects in an image
erosion = cv2.erode(img, kernel, iterations=5) # erosion is that it removes pixels at the boundaries of objects in an image
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel) # opening is just another name of erosion followed by dilation
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel) # closing is reverse of opening, dilation followed by erosion
mg = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel) # it is the difference between dilation and erosion of an image
th = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel) # it is the difference between input image and opening of the image


titles = ["image", "dilation", "erosion", "opening", "closing", "mg", "th"]
images = [img, dilation, erosion, opening, closing, mg, th]

for i in range(len(images)):
    plt.subplot(2,4,i+1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])  

plt.show()