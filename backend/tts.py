import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("ELEVEN_LABS")

VOICE_ID = "Cd34poZyG0jmSJD1fVJJ"


CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/{}".format(VOICE_ID)


headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": API_KEY
}


data = {
  "text": "You fucking donkey!",
  "model_id": "eleven_multilingual_v2",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.8,
    "style": 0.1
  }
}


response = requests.post(url, headers=headers, json=data)
with open('output.mp3', 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)
