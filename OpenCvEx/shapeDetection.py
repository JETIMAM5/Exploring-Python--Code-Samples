import cv2
import numpy as np

img = cv2.imread("shapes.jpg")  
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thres = cv2.threshold(imgGray, 240, 255, cv2.THRESH_BINARY)

# Konturları tespit et
contours, _ = cv2.findContours(thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    # Küçük konturları alan eşiğine göre filtrele
    if cv2.contourArea(contour) < 100:  # Alan eşiğini ihtiyaca göre ayarlayın
        continue

    # Kontur şeklinin yaklaşık şeklini hesapla
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)

    # Konturu çiz
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
    
    # Metni yerleştirmek için konum al
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10

    # Düzgün şekil tespiti ve etiketleme
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    elif len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        print(aspectRatio)
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            cv2.putText(img, "Square", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        else:
            cv2.putText(img, "Rectangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    elif len(approx) == 10:
        cv2.putText(img, "Star", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    else:
        cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

# Görüntüyü göster
cv2.imshow("Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
