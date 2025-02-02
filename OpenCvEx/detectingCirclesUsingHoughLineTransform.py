import cv2
import numpy as np  

# Read image
img = cv2.imread("smarties.png")

output = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 5)  # Apply blur to reduce noise

# Hough Circle Detection (Use blur instead of gray)
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, dp=1, minDist=20, 
                           param1=50, param2=30, minRadius=0, maxRadius=0)

# Check if any circles were detected
detected_circles = np.uint16(np.around(circles))
for x, y, r in detected_circles[0, :]:  # Loop through detected circles
    cv2.circle(output, (x, y), r, (0, 255, 0), 3)  # Draw outer circle
    cv2.circle(output, (x, y), 2, (0, 255, 255), 3)  # Draw center point
else:
    print("No circles detected. Try adjusting the parameters.")


# Display the result
cv2.imshow("Detected Circles", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
