import cv2
import pickle
try :
    with open('cars.pkl', 'rb') as f:
        liste=pickle.load(f)

except:
    liste=[]


def mouse(events,x,y,flags,param):
    if events==cv2.EVENT_LBUTTONDOWN:
        liste.append((x,y))

    if events==cv2.EVENT_RBUTTONDOWN:
        for i , pos in enumerate(liste):
            x1,y1 = pos
            if x1<x<x1+50 and y1<y<y1+24:
                liste.pop(i)

    with open("cars.pkl", "wb") as f:
        pickle.dump(liste,f)

while True:
    img= cv2.imread('photo1.png')
    print(liste)
    for l in liste:
        cv2.rectangle(img,l,(l[0]+50,l[1]+24),(255,0,0),2)
    cv2.imshow("Resim",img)
    cv2.setMouseCallback("Resim",mouse)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destoyAllWindows()