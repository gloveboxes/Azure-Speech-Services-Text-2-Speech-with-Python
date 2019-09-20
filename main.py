# https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support#text-to-speech
# https://docs.microsoft.com/en-au/azure/cognitive-services/Translator/reference/v3-0-languages?tabs=curl
# https://docs.microsoft.com/en-au/azure/cognitive-services/translator/language-support

import os
import time
import platform
from localise import Localize

# Uses PyGame on Windows and PyAudio on Linux and macOS
if platform.system() == 'Windows':
    from text2speech_windows import TextToSpeech
else:
    from text2speech import TextToSpeech

from text_translation import TextTranslation

speech_localisation_filename = 'speech_map_chinese.json'
# speech_localisation_filename = 'speech_map_korean.json'
# speech_localisation_filename = 'speech_map_japanese.json'

speechKey = None
translatorKey = None

try:
    speechKey = os.environ['SPEECHKEY']
    translatorKey = os.environ['TRANSLATOR_TEXT_KEY']
except:
    print("problem retrieving keys from environment variables")

localize = Localize(speech_localisation_filename)

t2s = TextToSpeech(azureSpeechServiceKey=speechKey, voice=localize.voice, enableMemCache=True, enableDiskCache=True)
tt = TextTranslation(azureTranslatorServiceKey=translatorKey, translateToLanguage=localize.translate, enableMemCache=True, enableDiskCache=True)

mandarin = tt.translate('You scanned a green apple')
t2s.play(mandarin)

mandarin = tt.translate('Neural voices provides very natural sounding speech')
t2s.play(mandarin)





t2s.play(localize.map('Starting scanner'))
time.sleep(0.5)

t2s.play('You scanned a green apple')
t2s.play(localize.map('Green Apple'))
time.sleep(0.5)

t2s.play(localize.map('Red Apple'))
time.sleep(0.5)

t2s.play(localize.map('Orange'))
time.sleep(0.5)

t2s.play(localize.map('Banana'))
