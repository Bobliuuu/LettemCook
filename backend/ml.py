import cv2
import PIL
from PIL import Image
import os
import datetime
import tts
import random


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

status = 2
last_warned = datetime.datetime.now()

NUM_CLIPS = 20
def get_voice_clip():
    num = random.randint(0, NUM_CLIPS)
    file_path = "voice_clips/output_{}.mp3".format(num)
    audio_length = tts.get_audio_length(file_path)
    return (file_path, audio_length)
    


while True:
    cur_time = datetime.datetime.now()
    
    # Read the frame
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    # status: 0 = not, 1 = +transition, 2 = yes, 3 = -transition
    
    paying_attention = False
    for (x, y, w, h) in faces:
        paying_attention = True
        if status == 0:
            # start attention transition
            attention_transition_start = datetime.datetime.now()
            status = 1
        elif w * h > 50000 and status == 3:
            # stop no attention transition
            status = 2
            no_attention_transition_start = None
        
        
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 6)
        cv2.putText(img, "paying attention", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 6)
    
    
    
    if not paying_attention:
        if status == 2:
            # start no attention transition
            no_attention_transition_start = cur_time
            status = 3
        elif status == 1:
            # stop attention transition
            status = 0
            attention_transition_start = None
    
    if status == 3 and (cur_time - no_attention_transition_start).total_seconds() > 5:
        status = 0
    elif status == 1 and (cur_time - attention_transition_start).total_seconds() > 3:
        status = 2
    
    if status == 1:
        cv2.putText(img, f"{3 - (cur_time - attention_transition_start).total_seconds():.2f}", (30, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 6)
    elif status == 3:
        cv2.putText(img, f"{5 -(cur_time - no_attention_transition_start).total_seconds():.2f}", (30, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)
    elif status == 0:
        cv2.putText(img, "not paying attention", (30, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)
        file_path, audio_length = get_voice_clip()
        if (cur_time - last_warned).total_seconds() > audio_length + 5:
            tts.play_audio(file_path)
            last_warned = cur_time
        
        

    # Display the video
    cv2.imshow('Face Detection', img)

    # Stop if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()
