import time

import gtts
from playsound import playsound
import pandas as pd
df = pd.read_csv('data/alphabet.csv')

words = list(df.sample_latinica)

for word in words:
#    tts = gtts.gTTS(f"{word}", lang="sr")
#    tts.save(f"sounds/{word}.mp3")
    playsound(f"sounds/{word}.mp3")
    time.sleep(1)
