import os
import json
from pathlib import Path

class Localize():

    def __init__(self, localization_filename):
        self.speech_map = None
        self.speech_voice = 'en-US-JessaNeural'
        self.speech_translate = None
        self.load_localisation(localization_filename)


    @property
    def voice(self):
        return self.speech_voice

    @property
    def translate(self):
        return self.speech_translate

    def load_localisation(self, localization_filename):
        if os.path.isfile(localization_filename):
            with open(localization_filename, encoding='utf-8') as f:
                json_data = json.load(f)
                self.speech_voice = json_data.get('voice')
                self.speech_translate = json_data.get('translate')
                self.speech_map = json_data.get('map')

    def map(self, key):
        value = key
        if self.speech_map is not None:
            result = list(
                filter(lambda text: text['key'] == key, self.speech_map))
            if len(result) > 0:
                value = result[0]['value']
        return value
