from text2speech import TextToSpeech
import os
from pathlib import Path

speechKey = os.environ['SPEECHKEY']
translatorKey = os.environ['TRANSLATOR_TEXT_KEY']


# https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support#text-to-speech
# https://docs.microsoft.com/en-au/azure/cognitive-services/Translator/reference/v3-0-languages?tabs=curl

t2s = TextToSpeech(azureSpeechServiceKey=speechKey, voice='ko-KR-HeamiRUS', azureTranslatorServiceKey=translatorKey, translateToLanguage='ko', enableMemCache=True, enableDiskCache=True)
t2s.play('granny smith scanned')
t2s.play('granny smith scanned')
t2s.play('red apple scanned')
t2s.play('orange scanned')
t2s.play('banana scanned')

t2s = TextToSpeech(azureSpeechServiceKey=speechKey, enableMemCache=True, enableDiskCache=True)
t2s.play("Starting scanner.")
t2s.play("You scanned a Red Delicious Apple.")
t2s.play("You scanned a Red Delicious Apple.")
t2s.play("You scanned a Granny Smith Apple.")
t2s.play("You scanned an Orange.")
t2s.play("You scanned a Banana.")
