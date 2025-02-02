import cv2
import datetime

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 30.0, (640,480))
print(cap.isOpened())
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3,3000)
cap.set(4,3000)

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "Width: " + str(cap.get(3)) + " " + "Height: " + str(cap.get(4))
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, datet, (10,50), font, 1, (0,255,255), 2,cv2.LINE_AA)
        out.write(frame)
        cv2.imshow('frame', frame)
        # cv2.imshow('frame1', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


cap.release()
out.release()
cv2.destroyAllWindows()

