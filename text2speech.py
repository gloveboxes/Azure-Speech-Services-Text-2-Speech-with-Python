from azure_speech import AzureSpeechServices
from azure_text_translate import TranslateText
from pygame import mixer
import time
import hashlib
from pathlib import Path
import os


class TextToSpeech():
    # Short name for 'Microsoft Server Speech Text to Speech Voice (en-US, GuyNeural)'
    def __init__(self, azureSpeechServiceKey, azureTranslatorServiceKey, translateTolanguage, voice='ko-KR-HeamiRUS',):
        self.translator = AzureSpeechServices(azureSpeechServiceKey, voice)
        self.translateText = TranslateText(
            azureTranslatorServiceKey, translateTolanguage)
        self.ttsAudio = {}
        mixer.init(frequency=16000, size=-16, channels=1)
        if not Path('.cache-audio').is_dir():
            os.mkdir('.cache-audio')

    def play(self, text):

        digest = hashlib.md5(text.encode()).hexdigest()
        audio = self.ttsAudio.get(digest)

        if audio == None:
            cacheFileName = ".cache-audio/{}.wav".format(digest)

            if Path(cacheFileName).is_file():
                with open(cacheFileName, 'rb') as audiofile:
                    audio = audiofile.read()
            else:
                translatedText = self.translateText.translate(text)

                if translatedText is None:
                    return

                audio = self.translator.get_audio(translatedText)

                if audio is not None:
                    with open('korean-{}'.format(text) + '.wav', 'wb') as audiofile:
                        audiofile.write(audio)
                    with open(cacheFileName, 'wb') as audiofile:
                        audiofile.write(audio)

            self.ttsAudio[digest] = audio

        self.sound = mixer.Sound(audio)
        self.sound.play()
        while mixer.get_busy():
            time.sleep(0.25)
