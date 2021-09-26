# Vancouver Datajam 2021 # team1

This repository contains a computer vision Python project developed by #team1

# Automated Fitness Tracker: Recovering from COVID Pandemic
## Project statement

During the COVID19 pandemic, many people were unable to attend recreational centres and fitness centers, and needed to rely on home tools. Furthermore, people experienced an increased sense of isolation and loss of motivation while working out at home. Some people might turn to a personal trainer who encourages them to continue physical training . In order to avoid further contact with strangers, and to ease social distancing measures, we are adapting a Python program that detects body pose with the purpose of helping people to count the repeated body exercises at home.

Our adaptation would help a person who is exercising count the number of repetitions of a given exercise they are doing, and also track their body posture as they exercise. Tracking body posture data can then be used to examine the movements that might cause injury.

## Project
This repository contains the jupyter notebooks and scripts for physical exercise classication and counting

## Data Collection
From all team members, videos of squat and bicep curls were collected and stored in this folder.
https://www.dropbox.com/sh/xdurn4e4y3rax54/AAB9wpGEhlyIALu861ZzSd5Ha?dl=0


## Data Extraction
50 frames containing medipipe pose joints were retrieved for each observation from each video. Data was stored into a csv. 

## Data Modelling and training
Normalize joint coordinates relative to center point of the body.
Structure input array to represent video frames per exercise repetiion
Build LSTM deep learning model, train and test.
Package model and create modular preprocessing package.
Create main script to ingest new video and predict with saved model.

## Prediction and counting
The counting.py library was created to count the number of moves in each type of exercise: squats and curls
## Project team members

Team lead: Nasreen Mohsin

Co-lead/ Mentor: Srishti Yadav

Mentor: Sami Mo

Documentation: Nasreen 

Scripting: Ketian Bai

Data extraction: Momo, Jason

Modelling and Training: Austin, Chloe, Sami

Sanity checking: 

## Vancouver Datajam 2021 Schedule:

### Main page: https://vancouverdatajam.ca/
#### Event format: 100% online

#### Important dates: 

|Date | Action item |
| - | - |
|Sep 13 - 17 |Participants are let in Discord, teams are formed|
|Sep 18 |[Workshop day!](https://www.vancouverdatajam.ca/workshops) Keynote: Making AI responsible with May Masoud|
|Sep 19 |Project statements are released|
|Sep 19-24 |Teams may work asynchronously (limited help desk support)|
|Sep 25 |Keynote talks, help desk support provided during the day, project submission deadline, career panel. See [speakers](https://www.vancouverdatajam.ca/speakers)|

#### Power up Saturday September 25 - suggested team schedule. All times in PDT

|Time| Action item|
| - | - |
|8:00 - 8:10| Land acknowledgement, opening remarks |
|8:10 - 8:40| Keynote: Role of Statistics in Data Science: Applications in Biomedical Sciences with Prof. Jemila Hamid | 
|8:40 - 9:10| Keynote: How to use the tools of data science to benefit Indigenous peoples and organizations  with Hannes Edinger |
|9:10 -  9:30| Keynote Q&A |
|9:30 | Help desk opens up, teams work on their project |
|9:30 - 10:00| Teams brainstorm tasks for the day|
|12:30 - 13:00| Team check in: share exploratory analysis results |
|15:30 - 16:00| Team check in: teams discuss presentation format and preliminary results|
|16:00 - 16:45| Teams prepare their 5-10 minute presentation, teams ensure all code is documented and stored in GitHub|
|17:00| Project video submission deadline|
|17:30 - 18:30| Project videos released on YouTube. Vote for your favourite team demo!| 
|18:30 - 20:00 | Career panel|
|20:00 - 20:30 | People's Choice Award presented. Closing remarks|
