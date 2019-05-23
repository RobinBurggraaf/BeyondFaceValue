from setup import SetupCam
#import dbSetup.py
import numpy as np
import cv2


setup = SetupCam()


# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
smileCascade = cv2.CascadeClassifier('Cascades/haarcascade_smile.xml')

previousSmiles = 0

setup.method_setup()
cap = setup.method_setup()

while True:
#    counter+=1
 #   print(counter)
    ret, frame = cap.read()
    #img = cv2.flip(img, -1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
    )

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
#        print("face found")
        smile = smileCascade.detectMultiScale(
            roi_gray,
            scaleFactor= 1.5,
            minNeighbors=15,
            minSize=(25, 25),
            )

        for (xx, yy, ww, hh) in smile:
            cv2.rectangle(roi_color, (xx, yy), (xx + ww, yy + hh), (0, 255, 0), 2)

        if len(smile) != previousSmiles or previousSmiles == 0:
            print("not smiling")
        else:
            print("you are now smiling")
        previousSmiles = len(smile)
    cv2.imshow('vide o', frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()
