import cv2
import numpy as np
import matplotlib.pyplot as plt

# Define the region of interest
def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    # channel_count = img.shape[2]
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def drawlines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), thickness=3)
    
    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img

# # read the image
# img = cv2.imread("PRoad.jpg")
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def process(img):
    # Defining the region of interest to ignore the distractions
    print(img.shape)
    height = img.shape[0]   
    width = img.shape[1]

    region_of_interest_vertices = [
        (0, height),
        (width/2 +10, height/2),
        (width, height)
    ]

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) 
    canny_image = cv2.Canny(gray, 100, 120) 
    crop_image = region_of_interest(canny_image, np.array([region_of_interest_vertices], np.int32)) 

    lines = cv2.HoughLinesP(crop_image, rho=2, theta = np.pi/60, threshold=50, lines=np.array([]), minLineLength=40, maxLineGap=100)
    image_with_lines = drawlines(img, lines)
    return image_with_lines

cap = cv2.VideoCapture("test_video.mp4")

while (cap.isOpened()):
    ret, frame = cap.read()
    frame = process(frame)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()