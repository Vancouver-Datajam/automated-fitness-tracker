import cv2
import numpy as np
import time
import PoseModule as pm
import glob
import csv



path = 'videos/*.*' # path of video directory
vid = 1 # start with video 1
NUM_CORDS = 32 # number of coordinates


# setup the table
landmarks = ['vid.no', 'obs.no', 'frame.no', 'pose'] #this is for the column headers
for x in range(0, NUM_CORDS+1):
    landmarks += ['x{}'.format(x), 'y{}'.format(x), 'z{}'.format(x)]

with open('coords.csv', mode='w', newline='') as f: #writing the columns to coords.csv
    csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(landmarks)

pose_name = "squats" #change this for each pose



# use glob to read files in a folder
for file in glob.glob(path):
    cap = cv2.VideoCapture(file)
    
    #out = cv2.VideoWriter('output_video.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 30, (1280, 720))
    #out = cv2.VideoWriter('output_video.mp4',-1, 30, (1280, 720))
    
    detector = pm.poseDetector()
    count = 0
    dir = 0
    pTime = 0
    obs = 1
    frame = 0


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
            #print(angle, per, bar)

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
            #print(count)

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
                    (255, 0, 0), 3)

        frame = frame + 1
                   
        
        #extract to csv
        try:
                # Extract Pose landmarks
                pose_row = list(np.array(lmList).flatten())
                
                # Append elements
                pose_row.insert(0, vid)
                pose_row.insert(1, obs)
                pose_row.insert(2, frame)
                pose_row.insert(3, pose_name)
                #pose_row.extend((vid,obs,frame,pose_name))
                
                # Export to CSV
                with open('coords.csv', mode='a', newline='') as f:
                    csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    csv_writer.writerow(pose_row) 
                
        except:
            pass
        
        #cv2.imshow("Image", img) 
        #out.write(img)
        #cv2_imshow(img)# to run in google colab
        #cv2.waitKey(1)


        if frame == 50:
            frame = 0
            obs = obs + 1


    cap.release()
    #out.release()
    vid = vid + 1
