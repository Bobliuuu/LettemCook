import google_vision
import os

print(os.getcwd())

google_vision.detect_text("backend/photos/lin_alg.png")