import cv2
import mouse as m
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
from time import sleep






kamera=cv2.VideoCapture(0)
kamera.set(cv2.CAP_PROP_FRAME_WIDTH,640)
kamera.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
detector=HandDetector(detectionCon=0.9,maxHands=1)


while True:

    kontrol,resim=kamera.read()
    hands,resim = detector.findHands(resim,flipType=False)
    cv2.rectangle(resim,(100,100),(580,380),(0,0,255),2)


    if hands:
        lmlist = hands[0]["lmList"]
        x1,y1=lmlist[5][0],lmlist[5][1]
        cv2.circle(resim,(x1,y1),7,(0,0,255),2)
        newx=int(np.interp(x1,(100,580),(0,1920)))
        newy = int(np.interp(y1, (100,380), (0, 1080)))
        x2, y2 = lmlist[8][0], lmlist[8][1]
        newex = int(np.interp(x2, (100, 540), (0, 1920)))
        newey = int(np.interp(y2, (100,380),(0,1080)))
        x3, y3 = lmlist[4][0], lmlist[4][1]
        neweex = int(np.interp(x3, (100, 540), (0, 1920)))
        neweey = int(np.interp(y3, (100, 380), (0, 1080)))
        m.move(newx,newy)
        mesafe=int(math.sqrt(math.pow(neweex-newex,2)+math.pow(neweey-newey,2)))
        print(mesafe)
        if mesafe <= 120:
            m.click("left")
            sleep(0.2)





    cv2.imshow("merhaba",resim)
    if cv2.waitKey(10)==27:
        break
