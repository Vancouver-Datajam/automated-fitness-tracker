#is similar to what is in the youtube video to detect poses

import cv2
import numpy as np
import time
import PoseModule as pm
import csv
from google.colab.patches import cv2_imshow

cap = cv2.VideoCapture("python-computer-vision/data/curls.mp4")
out = cv2.VideoWriter('output_video.mp4',cv2.VideoWriter_fourcc(*'MPV4'), 30, (1280, 720))
detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0

#momo=================
#first column is for pose "curls" and "squats"
num_coords = len(lmList) #number of coordinates (which should come out to 33 for the pose)
num_coords

landmarks = ['pose'] #this is for the column headers
for x in range(1, num_coords+1):
    landmarks += ['x{}'.format(x), 'y{}'.format(x), 'z{}'.format(x)]
landmarks

with open('coords.csv', mode='w', newline='') as f: #writing the columns to coords.csv
    csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(landmarks)

pose_name = "curls" #change this for each pose
#momo=================

while True:
    success, img = cap.read()
    if not success:
      break
    img = cv2.resize(img, (1280, 720))
    # img = cv2.imread("AiTrainer/test.jpg")
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    # print(lmList)
    if len(lmList) != 0:
        # Right Arm
        angle = detector.findAngle(img, 12, 14, 16)
        # # Left Arm
        #angle = detector.findAngle(img, 11, 13, 15,False)
        per = np.interp(angle, (210, 310), (0, 100))
        bar = np.interp(angle, (210, 310), (650, 100))
        # print(angle, per)

        # Check for the dumbbell curls
        color = (255, 0, 255)
        if per >=80: #100:
            color = (0, 255, 0)
            if dir == 0:
                count += 0.5
                dir = 1
        if per <=10: #0:
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

    
    ######---momo addition start
    #extract to csv
    try:
            # Extract Pose landmarks
            pose_row = list(np.array(lmList).flatten())
            pose_row
            
            # Append class name 
            pose_row.insert(0, pose_name)
            
            # Export to CSV
            with open('coords.csv', mode='a', newline='') as f:
                csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow(pose_row) 
            
    except:
        pass

    ####---momo addition start
    
    #cv2.imshow("Image", img) 
    out.write(img)
    #cv2_imshow(img)# to run in google colab
    #cv2.waitKey(1)
cap.release()
out.release()


