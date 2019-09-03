# https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support#text-to-speech
# https://docs.microsoft.com/en-au/azure/cognitive-services/Translator/reference/v3-0-languages?tabs=curl
# https://docs.microsoft.com/en-au/azure/cognitive-services/translator/language-support

import time
import json
from pathlib import Path
import os
import platform

# Uses PyGame on Windows and PyAudio on Linux and macOS
if platform.system() == 'Windows':
    from text2speech_windows import TextToSpeech
else:
    from text2speech import TextToSpeech

speech_localisation_filename = 'speech_map_chinese.json'
# speech_localisation_filename = 'speech_map_korean.json'
# speech_localisation_filename = 'speech_map_japanese.json'

speechKey = None
translatorKey = None


class Localize():

    def __init__(self, locatization_filename):
        self.speech_map = None
        self.speech_voice = 'en-US-JessaNeural'
        self.speech_translate = None
        self.load_localisation()

    @property
    def voice(self):
        return self.speech_voice

    @property
    def translate(self):
        return self.speech_translate

    def load_localisation(self):
        if os.path.isfile(speech_localisation_filename):
            with open(speech_localisation_filename, encoding='utf-8') as f:
                json_data = json.load(f)
                self.speech_voice = json_data.get('voice')
                self.speech_translate = json_data.get('translate')
                self.speech_map = json_data.get('map')

    def get_localised_text(self, key):
        value = key
        if self.speech_map is not None:
            result = list(
                filter(lambda text: text['key'] == key, self.speech_map))
            if len(result) > 0:
                value = result[0]['value']
        return value


try:
    speechKey = os.environ['SPEECHKEY']
    translatorKey = os.environ['TRANSLATOR_TEXT_KEY']
except:
    print("problem retrieving keys from environment variables")

localize = Localize(speech_localisation_filename)

t2s = TextToSpeech(azureSpeechServiceKey=speechKey, azureTranslatorServiceKey=translatorKey,
                   translateToLanguage=localize.translate,  voice=localize.voice, enableMemCache=True, enableDiskCache=True)

t2s.play('hello my name is dave')
t2s.play('Starting scanner')

t2s.play(localize.get_localised_text('Starting scanner'))
time.sleep(0.5)

t2s.play('You scanned a green apple')
t2s.play(localize.get_localised_text('Green Apple'))
time.sleep(0.5)

t2s.play(localize.get_localised_text('Red Apple'))
time.sleep(0.5)

t2s.play(localize.get_localised_text('Orange'))
time.sleep(0.5)

t2s.play(localize.get_localised_text('Banana'))
