import os, time
from shutil import copy2
from subprocess import Popen
import joint_capture


src = '/home/srishtiy/Downloads/exercise_video.webm' 
dest = '../webcam-data'

# Copy the downloaded file to current path
copy2(src, dest)

if not any(File.endswith(".webm") for File in os.listdir("../webcam-data")):
    time.sleep(5)
else:
    if __name__ == '__main__':
        joint_capture.save_video()

  
    
