# Библиотека gTTS использует гугловские технологии конвертации текста в речь. Не знаю где может быть полезно, но это действительно круто.
#
# Надо будет установить gTTS --> (тык)

from gtts import gTTS
import os
file = open("abc.txt", "r").read()

speech = gTTS(text=file, lang='en', slow=False)
speech.save("voice.mp3")
os.system("voice.mp3")