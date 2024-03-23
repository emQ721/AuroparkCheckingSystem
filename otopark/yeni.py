import cv2
import pickle
import numpy as np

cap = cv2.VideoCapture("video.mp4")


# Park alanlarını kontrol etmek için bir fonksiyon
def check(frame1):
    empty_spaces = 0
    occupied_spaces = 0
    for pos in liste:
        x, y = pos
        crop = frame1[y:y + 15, x:x + 26]
        count = cv2.countNonZero(crop)
        if count < 150:
            color = (0, 255, 0)  # Yeşil, boş park alanı
            empty_spaces += 1
        else:
            color = (0, 0, 255)  # Kırmızı, dolu park alanı
            occupied_spaces += 1
        cv2.rectangle(frame, pos, (pos[0] + 26, pos[1] + 15), color, 2)

    # Toplam kare sayısını ekrana yazdır
    total_spaces = len(liste)


    # Boş ve dolu park alanlarının sayısını ekrana yazdır
    cv2.putText(frame, f"Bos Park Sayisi: {empty_spaces}", (6, 335), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 2)
    cv2.putText(frame, f"Dolu Park Sayisi: {occupied_spaces}", (6, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 2)


# Kaydedilmiş park alanlarının yüklenmesi
with open("otopark.pickle", "rb") as f:
    liste = pickle.load(f)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 1)
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    median = cv2.medianBlur(thresh, 5)
    dilates = cv2.dilate(median, np.ones((3, 3), np.uint8), iterations=1)

    # Park alanlarının kontrol edilmesi
    check(dilates)

    # Görüntünün boyutunun değiştirilmesi
    frame_resized = cv2.resize(frame, (800, 800))

    # Görüntünün gösterilmesi
    cv2.imshow("asd", frame_resized)

    if cv2.waitKey(200) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
