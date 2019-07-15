from text2speech import TextToSpeech
import os
from pathlib import Path

speechKey = os.environ['SPEECHKEY']
translatorKey = os.environ['TRANSLATOR_TEXT_KEY']


# https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support#text-to-speech

t2s = TextToSpeech(speechKey, translatorKey, 'ko', 'ko-KR-HeamiRUS')

# t2s = TextToSpeech(key)

# t2s.play(" Hello, and welcome to Bits of Build. ")
t2s.play("Starting scanner.")
t2s.play("Starting scanner.")
t2s.play("You scanned a red apple.")
t2s.play("You scanned an orange.")
t2s.play("You scanned a banana.")
