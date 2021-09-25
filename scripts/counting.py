
import cv2
import numpy as np
import time
import PoseModule as pm
import time
import math


def counting_curls(detector,img,count,dir,pTime):
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    # print(lmList)
    if len(lmList) != 0:
        # Right arm
        angle = detector.findAngle(img, 12,14, 16)
        # # Left knee
        #angle = detector.findAngle(img, 11, 13, 15,False)
        per = np.interp(angle, (50, 150), (0, 100))
        bar = np.interp(angle, (50, 150), (650, 100))
        # print(angle, per)

        # Check for the dumbbell curls
        color = (255, 0, 255)
        if per >=80: #100:
            color = (0, 255, 0)
            if dir == 0:
                count += 0.5
                dir = 1
                print(count,dir)

        if per <=20: #0:
            color = (0, 255, 0)

            if dir == 1:
                count += 0.5
                dir = 0
                print(count)

        # Draw Bar
        cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
        cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
        cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                        color, 4)

        # Draw Curl Count
        cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15,
                        (255, 0, 0), 25)
        
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
                (255, 0, 0), 5)
    out.write(img)
    return count,dir,pTime

def counting_squat(detector,img,count,dir):
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    if len(lmList) != 0:
        # Right knee
        angle = detector.findAngle(img, 24, 26, 28)
        # # Left knee
        #angle = detector.findAngle(img, 23, 25, 27,False)
        per = np.interp(angle, (75, 180), (0, 100))
        bar = np.interp(angle, (75, 180), (650, 100))
        # print(angle, per)

        # Check for the dumbbell curls
        color = (255, 0, 255)
        if per >=80: #100:
            color = (0, 255, 0)
            if dir == 0:
                count += 0.5
                dir = 1
        if per <=25: #0:
            color = (0, 255, 0)
            if dir == 1:
                count += 0.5
                dir = 0
        # Draw Bar
        cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
        cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
        cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                        color, 4)

        # Draw Curl Count
        cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15,
                        (255, 0, 0), 25)
    
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
                (255, 0, 0), 5)
    
    return count,dir,pTime

