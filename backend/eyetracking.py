import cv2
from deepface import DeepFace
    
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')
cap = cv2.VideoCapture(-1)

while True:
    res, frame = cap.read()
    result = DeepFace.analyze(frame,actions = ['emotion'])
    emotions = result['emotion']
    print(emotions)
    # Lie detection below
    """
    lie = emotions['angry'] + emotions['disgust'] + emotions['fear'] + emotions['sad']
    truth = emotions['happy'] + emotions['surprise'] + emotions['neutral']
    if lie > truth:
        text = "Truth"
    else:
        text = "Stop lying to me you asshole"
    cv2.putText(frame, text, (50,50), font, 3, (255,0,0), 2, cv2.LINE_4)
    """
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

