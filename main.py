# https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support#text-to-speech
# https://docs.microsoft.com/en-au/azure/cognitive-services/Translator/reference/v3-0-languages?tabs=curl

from text2speech import TextToSpeech
import os
from pathlib import Path
import json
import time

speech_map = None
speech_voice = 'en-US-JessaNeural'

speech_localisation_filename = 'speech_map_chinese.json'
# speech_localisation_filename = 'speech_map_korean.json'


def load_localisation():
    global speech_map, speech_voice
    if os.path.isfile(speech_localisation_filename):
        with open(speech_localisation_filename, encoding='utf-8') as f:
            json_data = json.load(f)
            speech_voice = json_data.get('voice')
            speech_map = json_data.get('map')


def get_localised_text(key):
    value = key
    if speech_map is not None:
        result = list(filter(lambda text: text['key'] == key, speech_map))
        if len(result) > 0:
            value = result[0]['value']
    return value


speechKey = None
translatorKey = None

try:
    speechKey = os.environ['SPEECHKEY']
    translatorKey = os.environ['TRANSLATOR_TEXT_KEY']
except:
    print("problem retrieving keys from environment variables")




load_localisation()

t2s = TextToSpeech(azureSpeechServiceKey=speechKey,
                   voice=speech_voice, enableMemCache=True, enableDiskCache=True)

t2s.play(get_localised_text('Starting scanner'))
time.sleep(1)

t2s.play(get_localised_text('Green Apple'))
time.sleep(1)

t2s.play(get_localised_text('Red Apple'))
time.sleep(1)

t2s.play(get_localised_text('Orange'))
time.sleep(1)

t2s.play(get_localised_text('Banana'))
