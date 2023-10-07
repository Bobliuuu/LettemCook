import requests
from dotenv import load_dotenv
from classes import TTS_Request
import os

load_dotenv()
API_KEY = os.getenv("ELEVEN_LABS")

voice_ids = {
    "gordan_ramsay": "Cd34poZyG0jmSJD1fVJJ"
}


CHUNK_SIZE = 1024
tts_url = "https://api.elevenlabs.io/v1/text-to-speech/{}"


tts_headers = {
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
def get_data(text):
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.8,
            "style": 0.1
        }
    }
    return data
    


def get_tts(tts_request: TTS_Request):
    data = get_data(tts_request.text)
    url = tts_url.format(voice_ids[tts_request.voice])
    response = requests.post(url, headers=tts_headers, json=data)
    with open('output.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)