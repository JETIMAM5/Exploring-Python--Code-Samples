import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("messi5.jpg", cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3) # cv2.CV_64F is the data type of the output image, it should be kept as cv2.CV_64F, 
                                       # because the output of laplacian is negative and positive values, 
                                       # so we need to take the absolute value of the output
lap = np.uint8(np.absolute(lap))
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0) # 1 is the order of the derivative in x direction and 
                                          # 0 is the order of the derivative in y direction

sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)  

titles = ["image", "Laplacian", "sobelX", "sobelY", "sobelCombined"]
images = [img, lap, sobelX, sobelY, sobelCombined]

for i in range(len(images)):
    plt.subplot(2,3,i+1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()