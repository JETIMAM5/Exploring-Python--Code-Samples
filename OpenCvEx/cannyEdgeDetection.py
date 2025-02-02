import cv2
import numpy as np  
import matplotlib.pyplot as plt 

img = cv2.imread("messi5.jpg", 0)
canny = cv2.Canny(img, 100, 200) # 100 is the threshold1 and 200 is the threshold2

titles = ['image', 'canny']
images = [img, canny]

for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()