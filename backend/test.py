import tts
import random
import os

voice_lines = [
    "Get back to work you absolute imbecile! God damn it! You stupid buffoon!",
    "What are you doing? Get your head out of the clouds and back to the bloody work!",
    "This isn't a vacation! Move it! Time's ticking!",
    "Oi! Stop dawdling and get on with it!",
    "Do you think successful people got where they are by daydreaming? Back to work!",
    "Wake up! You've got things to do, and they won't do themselves!",
    "For heaven's sake, stop wasting precious time and put some effort into it!",
    "I've seen snails work faster than you right now! Get to it!",
    "If you spent as much time working as you do dilly-dallying, you'd be done by now!",
    "Enough with the distractions! Do you want success or not?",
    "Every second you waste, someone else is outworking you! Now, snap out of it and get back to it!"
]

for i in range(0, 11):
    print(os.getcwd())
    file_path = "voice_clips/output_{}.mp3".format(i)
    ramsay_tts = tts.TTS_Request(voice="gordan_ramsay", text=voice_lines[i])
    tts.get_tts(ramsay_tts, file_path)