import tts
from classes import TTS_Request

tts_1 = TTS_Request(id=0, voice="gordan_ramsay", text="Hello world!")
tts.get_tts(tts_1)