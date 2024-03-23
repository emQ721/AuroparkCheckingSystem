import cv2
import pickle
import numpy as np

cap = cv2.VideoCapture("video1.mp4")


def check(frame1):
    empty_spaces=0
    occupied_spaces=0
    for pos in liste:
        x,y = pos
        crop = frame1[y:y+24,x:x+50]
        count = cv2.countNonZero(crop)

        if count <100 :
            color =(0,255,0)
            empty_spaces+=1

        else:
            color = (0,0,255)
            occupied_spaces+=1

        cv2.rectangle(frame,pos,(pos[0]+50,pos[1]+24),color,2)

        total_spaces=len(liste)



with open ("cars.pkl","rb") as f :
    liste=pickle.load(f)


while True :

    _, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 1)
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    median = cv2.medianBlur(thresh, 5)
    dilates = cv2.dilate(median, np.ones((3, 3), np.uint8), iterations=1)

    check(dilates)


    frame_resized = cv2.resize(frame,(800,800))

    cv2.imshow("Camera",frame_resized)

    if cv2.waitKey(200) & 0xFF == ord('q'):
        break
cap.relase()
cv2.destroyAllWindows()





