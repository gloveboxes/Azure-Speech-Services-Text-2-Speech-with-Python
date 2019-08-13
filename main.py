from text2speech import TextToSpeech
import os
from pathlib import Path

speechKey = None
translatorKey = None

try:
    speechKey = os.environ['SPEECHKEY']
    translatorKey = os.environ['TRANSLATOR_TEXT_KEY']
except:
    print("problem retrieving keys from environment variables")


# https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support#text-to-speech
# https://docs.microsoft.com/en-au/azure/cognitive-services/Translator/reference/v3-0-languages?tabs=curl

t2s = TextToSpeech(azureSpeechServiceKey=speechKey, voice='ko-KR-HeamiRUS', enableMemCache=True, enableDiskCache=True)
t2s.play('빨간 사과 스캔')             # Red Apple
t2s.play('녹색 사과를 스캔하였습니다')  # Green Apple
t2s.play('오렌지를 스캔하였습니다')     # Orange
t2s.play('바나나를 스캔하였습니다')     # Banana


# t2s = TextToSpeech(azureSpeechServiceKey=speechKey, voice='ko-KR', enableMemCache=True, enableDiskCache=True)
t2s.play("빨간 사과 스캔")  # Red Apple
t2s.play("녹색 사과 스캔")  # Green Apple
t2s.play("오렌지 스캔")     # Orange
t2s.play("바나나 스캔")     # Banana
