#!/usr/bin/python
#Video Webcam capture for the Vancouver Datajam project 2021
# install opencv-python library
# run the script as python video_capture.py memberName_ExerciseClass_videoIndexNo_NumberOftimes
#Eg: python video_capture.py Nasreen_squat_01_6
# In this example, the video should show the squat motion in 6 times
import sys
import cv2
import time
filename=str(sys.argv[1])+'.mp4'
maxtime=20 # 20s video
cap= cv2.VideoCapture(0)

width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer= cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'DIVX'), 20, (width,height))

start_time = time.time()
while True:
    ret,frame= cap.read()

    writer.write(frame)

    cv2.imshow('frame', frame)
    end_time = time.time()

    if (end_time-start_time>=maxtime) or (cv2.waitKey(1) & 0xFF == 27): # either recording time is over or press esc
        break # stop recording


cap.release()
writer.release()
cv2.destroyAllWindows()