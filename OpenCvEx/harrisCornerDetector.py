import cv2
import numpy as np

# Check if the image is loaded correctly
img = cv2.imread("chessboard.png")

if img is None:
    print("Error: Image not loaded. Check the file path.")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    
    dst = cv2.cornerHarris(gray, 2, 3, 0.04)
    
    dst = cv2.dilate(dst, None)
    
    img[dst > 0.01 * dst.max()] = [0, 0, 255]
    
    cv2.imshow("Harris Corner Detector", img)
    
    if cv2.waitKey(0) & 0xFF == 27:
        cv2.destroyAllWindows()
