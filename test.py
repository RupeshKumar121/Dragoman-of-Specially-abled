import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
import time

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands = 1)
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")


offset = 20
imgSize = 300

folder = "Data/C"
counter = 0

recText = ""
recTime = 0

labels = ["M","I","S","Y","O","U","_","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]

while True:
    success,img = cap.read()
    imgOutput = img.copy()
    hands,img = detector.findHands(img)
    

    if hands:
        hand = hands[0]
        x,y,w,h = hand['bbox']

            
            
        imgWhite = np.ones((imgSize,imgSize,3),np.uint8)*255
        imgCrop = img[y-offset:y+h + offset , x - offset:x+w + offset]

        imgCropShape = imgCrop.shape

        aspectRatio = h/w

        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k*w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize - wCal)/2)
            imgWhite[0:imgResizeShape[0], wGap:wCal + wGap] = imgResize

            prediction, index = classifier.getPrediction(imgWhite,draw = False)
            recTime+=1
            if(recTime % 10 == 0):
                recTime = 0
                recText+=labels[index]
            
            
        else:
            k = imgSize / w
            hCal = math.ceil(k*h)
            imgResize = cv2.resize(imgCrop, (imgSize,hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - hCal)/2)
            imgWhite[hGap:hCal + hGap, : ] = imgResize
            
            prediction, index = classifier.getPrediction(imgWhite,draw = False)
            
            recTime+=1
            if(recTime>=95):
                recTime = 0
                recText+=labels[index]

        
        cv2.rectangle(imgOutput, (x- offset,y - offset - 55), (x-offset + 100, y- offset ), (255,0,255),cv2.FILLED)
        cv2.putText(imgOutput, labels[index] , (x,y-26),cv2.FONT_HERSHEY_COMPLEX, 1.7, (255,255,255),2)
        cv2.rectangle(imgOutput, (x- offset,y - offset), (x+w + offset, y+h+offset), (255,0,255), 4)
        cv2.rectangle(imgOutput, (0,500), (500, 600), (255,255,255), cv2.FILLED)

       
       
        
            
        cv2.imshow("ImageCrop", imgCrop)
        cv2.imshow("ImageWhite", imgWhite)

    print(recText)

    cv2.rectangle(imgOutput, (0,430), (640, 480), (255,255,255),cv2.FILLED)
    cv2.putText(imgOutput,recText , (5,467),cv2.FONT_HERSHEY_COMPLEX, 1.3, (255,0,255),2)    
     
    cv2.imshow("Image",imgOutput)
    cv2.waitKey(1)
    

