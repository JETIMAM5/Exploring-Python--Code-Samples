import cv2
import numpy as np 

cap = cv2.VideoCapture(0)
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG2()
while True:
    ret, frame = cap.read()
    if frame is None:
        break

    keyboard = cv2.waitKey(30)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()