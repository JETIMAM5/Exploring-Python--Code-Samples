# import matplotlib
import cv2
# import numpy as np
# # import matplotlib.pyplot as plt
# matplotlib.use('TkAgg')  # PyCharm'da grafiklerin doğru bir şekilde gösterilmesi için backend'i 'TkAgg' olarak değiştiriyoruz
# -------------------------------------------------------------------------------------------
# Reading an image
# We'e reading 'who.jpg' as a gray image
# cv2.IMREAD_GRAYSCALE, reads the image as gray image.
# img = cv2.imread('who.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('lena.jpg') # this reads image as colored
# -------------------------------------------------------------------------------------------
# READING IMAGE WITH OPENCV
# cv2.imshow("image", img)
# h, w = img.shape[:2] # Takes 2 channels of image  (1-Height, 2-Width, 3-Color channel)
# cv2.waitKey(0)  # Closes the window if any key is pressed
# print(f"Height: {h}, Width: {w}")
# cv2.destroyAllWindows()  # Closes all windows
# -------------------------------------------------------------------------------------------
# SHOWING IMAGE WITH MATPLOTLIB
# 'cmap="gray"' we're using gray map with this
# 'interpolation="bicubic"' helps enhance the quality of image (optional).
# plt.imshow(img, cmap="gray", interpolation="bicubic")
# plt.plot([50, 150], [120, 320], 'c', linewidth=5)
# plt.show()
# -------------------------------------------------------------------------------------------
# cv2.imwrite('WirstWatch.jpg', img) # SAVES THE FILE
# -------------------------------------------------------------------------------------------
# Extracting RGB values.
# Here we have randomly chosen a pixel
# by passing in 100, 100 for height and width.
# OpenCV uses R G B  in  B G R order
# (B, G, R) = img[100, 100]
# -------------------------------------------------------------------------------------------
# DISPLAYING THE PIXEL VALUES
# print("R = {}, G = {}, B = {}".format(R, G, B))
# -------------------------------------------------------------------------------------------
# WE CAN ALSO PASS THE VALUE TO EXTRACT THE VALUE FOR A SPECIFIC CHANNEL
# B = img[100, 100, 0]
# print("B = {}".format(B))
# -------------------------------------------------------------------------------------------
# WE'LL CALCULATE THE REGION OF INTEREST BY SLICING THE PIXELS OF IMAGE
# roi = img[100: 500, 200: 700]
# cv2.imshow("ROI", roi)
# cv2.waitKey(0)
# --------------------------------------------------------------------------------------------
# WE CAN RESIZE THE IMAGE
# resize = cv2.resize(img, (500, 700))
# cv2.imshow("resize", resize)
# cv2.waitKey(0)
# -------------------------------------------------------------------------------------------
# MAINTAIN A PROPER ASPECT RATIO
# ratio = 800 / w
# dim = (800, int(h * ratio))
#
# resize_aspect = cv2.resize(img, dim)
# cv2.imshow('Resized image', resize_aspect)
# cv2.waitKey(0)
# -------------------------------------------------------------------------------------------
# DRAWING A RECTANGLE (Image, Top-left corner co-ordinates, Bottom-right corner co-ordinates, Color (in BGR format),
# Line width) --> This is the order of rectangle() function
# output = img.copy()
# rectangle = cv2.rectangle(img, (100, 500), (200, 200), (255, 0, 0), 2)
# cv2.imshow('rectangle', rectangle)
# cv2.waitKey(0)
# -------------------------------------------------------------------------------------------
# DISPLAYING A TEXT
# Arguments of putText() function -->
# image , text to be displayed , Bottom-left corner co-ordinates, from where the text should start ,Font
# Font size ,Color (BGR format), Line width
# output = img.copy()
# text = cv2.putText(output, "MerhabalarGonulDostlari", (350, 290), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
# cv2.imshow('Image With Text', output)
# cv2.waitKey(0)
# -------------------------------------------------------------------------------------------
# print(img) # prints image as matrix
# cv2.imshow('img', img)
# k = cv2.waitKey(0)
# if k == 27:
#     cv2.destroyAllWindows()
# elif k == ord('s'):
#     cv2.imwrite('lena_copy.jpg', img)
#     cv2.destroyAllWindows()








